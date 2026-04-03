#include <stdio.h>
#include <cs50.h>

int main(void)
{
    char *s = "Hi!";
    //printf("%p\n", s);
    //printf("%p\n", &s[0]);
    //printf("%p\n", &s[1]);
    //printf("%p\n", &s[2]);
    //printf("%p\n", &s[3]);
    printf("%c\n", *s);
    printf("%c\n", *(s + 1));


    /*
    int n = 50;
    int *p = &n;
    printf("Value: %i\n", n);
    printf("Adress: %p\n", p);
    printf("Value: %i\n", *p);
    */
}
