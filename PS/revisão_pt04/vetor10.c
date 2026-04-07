#include <stdio.h>

void main(void){
    int vector[10] = {0*10};

    vector[0] = 2;
    vector[1] = 1;
    vector[2] = 2;
    vector[3] = 1;
    vector[4] = 2;
    vector[5] = 1;
    vector[6] = 2;
    vector[7] = 1;
    vector[8] = 2;
    vector[9] = 1;
    
    int somapar = vector[0]+vector[2]+vector[4]+vector[6]+vector[8];
    int somaimpar = vector[1]+vector[3]+vector[5]+vector[7]+vector[9];

    printf("Soma dos indices pares: %i \n", somapar);
    printf("Soma dos indices impares: %i", somaimpar);
}