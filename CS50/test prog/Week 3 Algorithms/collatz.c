#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <ctype.h>

int collatz(int n);
bool check_arg(const char *s);

int main(int argc, string argv[])
{
    int ans = 0;
    if (argc == 2 && check_arg(argv[1]))
    {

        ans = collatz(atoi(argv[1]));
        printf("Ans: %i\n", ans);
    }
    else if (argc == 1)
    {
        int num = get_int("Insert Number: ");
        ans = collatz(num);
        printf("Ans: %i\n", ans);
    }
    else
    {
        printf("Invalid argument: \n");
        return 1;
    }
    return 0;
}

int collatz(int n)
{
    if (n == 1)
    {
        return 0;
    }
    else if ((n % 2) == 0)
    {
        return 1 + collatz(n / 2);
    }
    else
    {
        return 1 + collatz(3*n + 1);
    }
}

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
