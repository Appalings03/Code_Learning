#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node
{
    string phrase;
    struct node *next;
} node;

#define LIST_SIZE 2

bool unload (node *list);
void visualizer(node *list);

int main(void)
{
    node *list = NULL;

    for (int i = 0; i < LIST_SIZE; i++)
    {
        string phrase = get_string("Enter a new phrase: ");

        node *n = malloc(sizeof(node));
        if ( n == NULL)
        {
            free(list);
            return 1;
        }

        n -> phrase = phrase;
        n -> next = list;
        list = n;

        visualizer(list);
    }

    if (!unload(list))
    {
        printf("Error freeing the list.\n");
        return 1;
    }

    printf("Freed the list.\n");
    return 0;
}

bool unload (node *list)
{
    node *ptr = list;

    while (ptr != NULL)
    {
        ptr = list -> next;
        free(list);
        list = ptr;
    }
    return true;
}

void visualizer(node *list)
{
    printf("\n+-- List Visualizer --+\n\n");
    while(list != NULL)
    {
        printf("Location: %p\n", list);
        printf("Phrase: %s\n", list -> phrase);
        printf("Next: %p\n\n", list -> next);
        list = list -> next;
    }
    printf("+---------------------+\n\n");
    return;
}
