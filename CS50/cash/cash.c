#include <cs50.h>
#include <stdio.h>

void luhnAlgo(int change);

int main(void)
{
    int change;
    do
    {
        change = get_int("Change owed: ");
    }
    while (change < 0);

    if (change == 0)
    {
        printf("0\n");
    }
    else
    {
        luhnAlgo(change);
    }
    return 0;
}

void luhnAlgo(int change)
{
    int counter = 0, counQ = 0, counD = 0, CounN = 0, counP = 0;

    // quarters ($0.25)
    while (change >= 25)
    {
        counQ++;
        change = change - 25;
    }
    // dimes ($0.10)
    while (change >= 10)
    {
        counD++;
        change = change - 10;
    }
    // nickels ($0.05)
    while (change >= 5)
    {
        CounN++;
        change = change - 5;
    }
    // pennies ($0.01)
    while (change >= 1)
    {
        counP++;
        change = change - 1;
    }
    counter = counQ + counD + CounN + counP;
    printf("%i\n", counter);
}
