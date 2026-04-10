#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main(){
    srand(time(NULL));
    int tam = 0;
    printf("Insira o tamanho dos vetores: ");
    scanf("%i", &tam);

    int v1[tam];
    int v2[tam];

    printf("\n v1 = [");
    for (int i = 0;i < tam;i++){
        v1[i] = rand()% 5;
        printf("%i,", v1[i]);
    }
    printf("]\nv2 = [");
    for (int i = 0;i < tam;i++){
        v2[i] = rand()% 5;
        printf("%i,", v2[i]);
    }
    printf("]");

    int p_esc[tam];

    printf("\n produto escalar = [");
    for (int i = 0;i < tam;i++){
        p_esc[i] = v1[i] * v2[i];
        printf("%i,", p_esc[i]);
    }
    printf("]\n");
}