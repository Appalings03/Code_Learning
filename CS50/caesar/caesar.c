#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void cypher(string s, int k);
bool check_arg(const char *s);

int main(int argc, string argv[])
{
    // verify for 2 argv and for non digit
    if (argc == 2 && check_arg(argv[1]))
    {
        int key = atoi(argv[1]);
        string ptext = get_string("plaintext: ");
        cypher(ptext, key);
    }
    else
    {
        // return 1 if no argv provided
        printf("Usage: ./caesar k\n");
        return 1;
    }
    return 0;
}

// function to cypher the word or sentences
void cypher(string s, int k)
{
    // allocate memory for the string that contains the cypher word
    string code = malloc(10 * strlen(s));
    // loop for each char in the string
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        // verify if the letter is in lowercase or uppercase or add the non letter in the final
        // string
        if (s[i] >= 'a' && s[i] <= 'z')
        {
            code[i] = (((s[i] - 'a') + k) % 26) + 'a';
        }
        else if (s[i] >= 'A' && s[i] <= 'Z')
        {
            code[i] = (((s[i] - 'A') + k) % 26) + 'A';
        }
        else
        {
            code[i] = s[i];
        }
    }
    // print the cypher
    printf("ciphertext: %s\n", code);
}

// function to loook at all the char in the argv[1]
bool check_arg(const char *s)
{
    while (*s)
    {
        if (!isdigit((unsigned char) *s))
        {
            // return false if a non digit is found
            return false;
        }
        s++;
    }
    // return true if there is only digit
    return true;
}
