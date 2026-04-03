#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void cypher(string s, string k, int len);
char substitut(char pos, string key);
bool check_arg(string s, int l);

int main(int argc, string argv[])
{
    if (!(argc == 2))
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    int len = strlen(argv[1]);
    if (!(len == 26))
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    string key = argv[1];
    if (check_arg(argv[1], len))
    {
        return 1;
    }

    string ptext = get_string("plaintext: ");
    cypher(ptext, key, strlen(ptext));
    return 0;
}

void cypher(string s, string k, int len)
{

    string code = malloc(10 * strlen(s));
    for (int i = 0; i < len; i++)
    {
        if (isalpha(s[i]))
        {
            char x = s[i];
            if (islower(s[i]))
            {
                code[i] = substitut(tolower(x), k);
            }
            else
            {
                code[i] = substitut(toupper(x), k);
            }
        }
        else
        {
            code[i] = s[i];
        }
    }
    printf("ciphertext: %s\n", code);
}

char substitut(char pos, string key)
{
    string alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int l = strlen(alpha);
    for (int i = 0; i < l; i++)
    {
        if (islower(pos))
        {
            if (pos == tolower(alpha[i]))
            {
                return tolower(key[i]);
            }
        }
        else
        {
            if (pos == toupper(alpha[i]))
            {
                return toupper(key[i]);
            }
        }
    }
    return pos;
}

// function to loook at all the char in the argv[1]
bool check_arg(string s, int l)
{
    for (int i = 0; i < l; i++)
    {
        if (!isalpha(s[i]))
        {
            printf("Key must contain 26 characters.\n");
            return true;
        }
        for (int j = i + 1; j < l; j++)
        {
            // printf("Comparing %c and %c\n", s[i], s[j]);
            if (toupper(s[j]) == toupper(s[i]))
            {
                printf("Key must not contain repeated alphabets.\n");
                return true;
            }
        }
    }
    return false;
}
