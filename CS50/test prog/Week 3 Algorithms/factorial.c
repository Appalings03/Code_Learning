#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <ctype.h>

int factorial(int n);

int main(int argc, string argv[])
{
    int ans = 0;
    if (argc == 2 && check_arg(argv[1]))
    {
        ans = factorial(atoi(argv[1]));
        printf("Ans: %i\n", ans);
    }
    else if (argc == 1)
    {
        int num = get_int("Insert Number: ");
        ans = factorial(num);
        printf("Ans: %i\n", ans);
    }
    else
    {
        printf("Invalid argument\n");
        return 1;
    }
    return 0;
}

int factorial(int n)
{
    if (n ==1)
        return 1;
    else
        return n * factorial(n - 1);

}
/*
int factorial(int n)
{
    int prod = 1;
    while (n > 0)
    {
        prod *= n;
        n--;
    }
    return prod;
}
*/
