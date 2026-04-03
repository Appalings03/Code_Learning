#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

void get_count(string text, int len, int combine[]);
void get_grade(int l, int w, int s);

int main(void)
{
    int combine[3];
    string text = get_string("Text: ");

    int length = strlen(text);
    get_count(text, length, combine);

    // verify the count
    // printf("letter %i\n", combine[0]);
    // printf("word %i"\n, combine[1]);
    // printf("sentences %i\n", combine[2]);

    // get the result of the grade
    get_grade(combine[0], combine[1], combine[2]);
}

void get_grade(int l, int w, int s)
{
    // calculate average and index
    float L = ((float) l / (float) w) * 100;
    float S = ((float) s / (float) w) * 100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);

    // check index
    // printf("index: %i\n", index);
    // check grade
    if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

void get_count(string text, int len, int combine[])
{
    int letters = 0;
    int word = 0;
    int sentences = 0;

    for (int i = 0; i < len; i++)
    {
        char c = text[i];
        // count letters from text
        if (isalpha(c) != 0)
        {
            letters++;
        }
        // count word-1 from the text
        if (c == ' ')
        {
            word++;
        }
        // count sentence from the text
        if (c == '.' || c == '?' || c == '!')
        {
            sentences++;
        }
    }
    // add the last word
    word += 1;

    // Didn't use a loop because it's only 3 value
    combine[0] = letters;
    combine[1] = word;
    combine[2] = sentences;
}
