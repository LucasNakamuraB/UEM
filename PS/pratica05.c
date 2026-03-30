#include <stdio.h>

void main(){
    int num1 = 0;
    int num2 = 0;
    
    printf("Insira o numero 1:");
    scanf("%i", &num1);
    printf("\nInsira o numero 2:");
    scanf("%i", &num2);
    if (num1 > num2){
        printf("%i, %i", num1, num2);
    }
    else{
        printf("%i, %i", num2, num1);

    }
}
