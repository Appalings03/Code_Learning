#include <cs50.h>
#include <stdio.h>

// AMEX 15         STRT 34 OR 37
// MC   16         STRT 51, 52, 53, 54, 55
// VISA 13 OR 16   STRT 4

int luhnAlgo(long int card);
long power(int n, int p);

int main(void)
{
    long int card;
    int sum = 0;

    do
    {
        card = get_long("Card Number: ");
    }
    while (card < 1);

    int amex = card / power(10, 13);
    int master = card / power(10, 14);
    int visa1 = card / power(10, 12);
    int visa2 = card / power(10, 15);

    sum = luhnAlgo(card);

    // check type
    if (sum % 10 == 0)
    {
        if (amex == 34 || amex == 37)
        {
            printf("AMEX\n");
        }
        else if (master == 51 || master == 52 || master == 53 || master == 54 || master == 55)
        {
            printf("MASTERCARD\n");
        }
        else if (visa1 == 4 || visa2 == 4)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
    return 0;
}

// Luhn Algo
int luhnAlgo(long int card)
{
    int sum = 0;
    int digit_count = 0;
    while (card > 0)
    {
        int digit = card % 10;
        card /= 10;
        digit_count++;

        if (digit_count % 2 == 0)
        {
            digit *= 2;
            if (digit > 9)
            {
                digit -= 9;
            }
        }
        sum += digit;
    }
    return sum;
}

long power(int n, int p)
{
    long result = 1;
    for (int i = 0; i < p; i++)
    {
        result = result * n;
    }
    return result;
}
