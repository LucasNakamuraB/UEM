#include <stdio.h>

void main(){
    int ini1;
    printf("Início do segemnto 1:");
    scanf("%i", &ini1);
    int fim1;
    printf("Fim do segmento 1:");
    scanf("%i", &fim1);
    int ini2;
    printf("Início do segmento 2:");
    scanf("%i", &ini2);
    int fim2;
    printf("Fim do segmento 2:");
    scanf("%i", &fim2);

    int inter_ini;
    int inter_fim;

    int s1_ed = 0;
    int s2_ed = 0;

    int intersect = 0;

    if (ini1<fim1){s1_ed = 1;}
    if (ini2<fim2){s2_ed = 1;}
    
    if (s1_ed && s2_ed){
        if (fim1>ini2){
            inter_ini = ini2;
            inter_fim = fim1;
        }
    }
    else if (!s1_ed && s2_ed){
        if (ini1>ini2){
            inter_ini = ini2;
            inter_fim = ini1;
        }
    }
    else if (!s1_ed && !s2_ed){
        if (ini1>fim2){
            inter_ini = fim2;
            inter_fim = ini1;
        }
    }
    else if (s1_ed && !s2_ed){
        if (fim1>fim2){
            inter_ini = fim2;
            inter_fim = fim1;
        }
    }
    printf("Intersecção: inicio(%i) fim(%i)", inter_ini, inter_fim);
}