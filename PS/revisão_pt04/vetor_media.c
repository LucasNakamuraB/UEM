#include <stdio.h>

void main(){
    int n = 0;
    printf("insira o tamanho do vetor:");
    scanf("%i", &n);

    float vector[n];
    float buffer;
    for (int i = 0; i < n; i++){
        printf("insira o valor do indice %i:", i);
        scanf("%f", &buffer);
        int diff = 0;
        for (int i = 0; i < n; i++){if(buffer == vector[i]){diff = 1;}}
        if (diff == 1){
            i--;
            printf("o numero nao pode ser repetido! \n");
        }
        else{
            vector[i] = buffer;
        }
    }
    int i = 0;
    float soma = 0;
    while (i<n){
        soma += vector[i];
        i++;
    }
    float media = soma / n;

    float menor = vector[0];
    float maior = vector[0];
    i = 0;
    do{
        if (vector[i] < menor){menor = vector[i];}
        if (vector[i] > maior){maior = vector[i];}
        i++;
    }
    while (i < n);

    printf("media dos valores: %.2f\n", media);
    printf("maior numero: %.2f\n", maior);
    printf("menor numero: %.2f\n", menor);
    

}