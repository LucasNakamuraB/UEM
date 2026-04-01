#include <stdio.h>

void main(void){
    int n = 0;
    printf("Quantas casas de fibonacci calcular?: ");
    scanf("%i", &n);
    int contador = 1;
    int ultimo = 1;
    int penultimo = 0;
    printf("1");
    do{
        int new = ultimo + penultimo;
        printf("%i", new);
        penultimo = ultimo;
        ultimo = new;
        contador++;
    }
    while (contador<=n);
}