#include <stdio.h>
#include <cs50.h>

int main(void){
    string ans = get_string("What's your name?\nAnswer: ");
    printf("Hello, %s\n", ans);
    return 0;
}
