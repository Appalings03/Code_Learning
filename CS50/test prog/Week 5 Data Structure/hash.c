#include <ctype.h>

int hash(char *word)
{
    return toupper(word[0]) - 'A';
}
