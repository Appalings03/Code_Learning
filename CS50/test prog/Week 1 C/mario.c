#include <stdio.h>
#include <cs50.h>

void print_row(int n);
int main(void){
    do{
        int height = get_int ("What is the height of the pyramid? ");
    }while(height < 1)

    for (int i = 0; i < 3; i++){
        print_row(3);
    }
}

void print_row(int n){
    for (int i = 0; i < n; i++){
        printf("#");
    }
    printf("\n");
}

void print_row(int bricks){
    printf("#")
}
