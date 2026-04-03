// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// TODO: Choose number of buckets in hash table
#define N 10000
#define LENGTH 45

unsigned int count = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    char lower_word[LENGTH + 1];
    int len = strlen(word);
    // convert word to lower
    for (int i = 0; i < len; i++)
    {
        lower_word[i] = tolower(word[i]);
    }
    lower_word[len] = '\0';

    unsigned int index = hash(lower_word);

    node *ptr = table[index];
    while (ptr != NULL)
    {
        if (strcasecmp(ptr->word, lower_word) == 0)
            return true;

        ptr = ptr->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // use djb2 by Dan Bernstein to hash the word.
    unsigned long hash = 5381;
    int c;
    while ((c = *word++))
    {
        hash = ((hash << 5) + hash) + tolower(c);
    }
    return hash % N;
    // other hash function
    // FNV-1a
    /*
        unsigned int hash = 2166136261u;
        for (int i = 0; word[i] != '\0'; i++)
        {
            hash ^= tolower(word[i]);
            hash *= 16777619;
        }
        return hash % N;
    */
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
        return false;

    char word[LENGTH + 1];

    while (fscanf(dict, "%45s", word) != EOF)
    {
        node *dict_node = malloc(sizeof(node));
        if (dict_node == NULL)
        {
            fclose(dict);
            return false;
        }

        strcpy(dict_node->word, word);
        dict_node->next = NULL;

        unsigned int index = hash(word);

        dict_node->next = table[index];
        table[index] = dict_node;
        // don't forget to increase count
        count++;
    }
    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    // Use the principle of unload memory seen in section 5 and adjust it with while loop to empty
    // all the linked list
    for (int i = 0; i < N; i++)
    {
        node *ptr = table[i];

        while (ptr != NULL)
        {
            node *tmp = ptr;
            ptr = ptr->next;
            free(tmp);
        }
        // clean table
        table[i] = NULL;
    }
    return true;
}
