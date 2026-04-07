#include <stdio.h>

void main(){
    int num1 = 0;
    int num2 = 0;
    int num3 = 0;
    
    printf("Insira o numero 1:");
    scanf("%i", &num1);
    printf("\nInsira o numero 2:");
    scanf("%i", &num2);
    printf("\nInsira o numero 3:");
    scanf("%i", &num3);
    if (num1 > num2){
        if (num2 > num3){
            printf("%i, %i, %i", num1, num2, num3);
        }
        else{
            printf("%i, %i, %i", num1, num2, num3);

        }
    }
    else if(num2 > num1 && num2>num3){
        if (num1 > num3){
            printf("%i, %i, %i", num2, num1, num3);

        }
        else{
            printf("%i, %i, %i", num2, num3, num1);

        }

    }
    else if(num3 > num2 && num3 > num1){
        if (num1 > num2){
            printf("%i, %i, %i", num3,num1, num2);
        }
        else{
            printf("%i, %i, %i", num3, num2, num1);

        }
    }
}
