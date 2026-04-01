#include <stdio.h>

void main(){
    int n = 0;
    printf("Quantos numeros quer calcular?: ");
    scanf("%i", &n);
    int contador = 1;
    float soma = 0;
    float buffer = 0;
    float maior = 0;
    float menor = 0;

    for (contador = 1; contador <= n; contador++){
        printf("Insira o numero #%i: ", contador);
        scanf("%f", &buffer);
        soma = soma + buffer;
        
        if (contador == 1  || buffer > maior){
            maior = buffer;
        }
        if (contador == 1 || buffer < menor){
            menor = buffer;
        }
    }

    printf("Soma: %f \n", soma);
    printf("Media: %f \n", soma/n);
    printf("Maior: %f \n", maior);
    printf("Menor: %f \n", menor);

}