#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define SIZE 512
typedef uint8_t BYTE;

int jpeg(BYTE temp[]);

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover card.raw\n");
        return 1;
    }
    // create variables
    char *f = argv[1];
    BYTE temp[SIZE];
    // Open the memory card
    FILE *input = fopen(f, "r");
    FILE *output = NULL;
    char name[8];
    int count = 0;

    // verify input not NULL
    if (input == NULL)
    {
        printf("Could not open %s\n", f);
        return 1;
    }

    // While there's still data left to read from the memory card
    while (fread(temp, SIZE, 1, input) == 1)
    {
        if (jpeg(temp) == 1)
        {
            if (output != NULL)
                fclose(output);
            // Create JPEGs from the data
            sprintf(name, "%03i.jpg", count++);
            output = fopen(name, "w");
            // check img creation
            if (output == NULL)
            {
                printf("Could not create %s\n", name);
                fclose(input);
                return 1;
            }
            fwrite(temp, SIZE, 1, output);
        }
        else if (output != NULL)
        {
            // continue to write in open file
            fwrite(temp, SIZE, 1, output);
        }
    }
    // close file
    fclose(input);
    if (output != NULL)
        fclose(output);

    return 0;
}

int jpeg(BYTE temp[])
{
    BYTE signature[] = {0xff, 0xd8, 0xff};

    for (int i = 0; i < 3; i++)
    {
        if (temp[i] != signature[i])
        {
            return 0;
        }
    }
    if ((temp[3] & 0xf0) == 0xe0)
        return 1;
    return 0;
}
