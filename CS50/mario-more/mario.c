#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;

    do
    {
        height = get_int("Height: ");
    }
    while (height < 1);

    for (int i = 0; i < height; i++)
    {

        for (int space = 1; space < (height - i); space++)
        {
            printf(" ");
        }

        for (int j = 0; j < (i + 1); j++)
        {
            printf("#");
        }

        printf("  ");

        for (int j = 0; j < (i + 1); j++)
        {
            printf("#");
        }

        printf("\n");
    }
    return 0;
}
