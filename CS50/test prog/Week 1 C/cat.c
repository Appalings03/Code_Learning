#include <stdio.h>
#include <cs50.h>

void meow(int n);
int get_positive_int(void);

int main(void){
    /*int i = 0;
    while(i < 3)
    {
        printf("meow\n");
        i++;
    }*/
    int n = get_positive_int();
    meow(n);
}

int get_positive_int (void){
    int n;
    do{
        n = get_int("Number: ");
    }while (n < 1);
    return n;
}


void meow(int n){
    for(int j = 0; j < n; j++){
        printf("meow\n");
    }
}
