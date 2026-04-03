#include <cs50.h>
#include <stdio.h>

int main(void){
    long dollars = 1;
    while (true){
        char c = get_char("Here's $%li. Double it and give it to the next person? ", dollars);
        if (c 'y'){
            dollars *= 2;
        }else{
            break;
        }
    }
    printf("Here's $%li.\n", dollars);
}
/* Truncation
int x = get_int("x: ");
int y = get_int("y: ");
printf("%.5f\n", (float) x / y);
*/
