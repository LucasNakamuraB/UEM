#include <stdio.h>

void main(void){
    int run = 1;
    while (run){

        int size;
        printf("insira o tamanho dos vetores:");
        scanf("%i", &size);
        float v1[size];
        float v2[size];

        for (int i = 0;i < size; i++){
            printf("Insira o valor %i do vetor 1", i);
            scanf("%f", v1[i]);
        }
        for (int i = 0;i < size; i++){
            printf("Insira o valor %i do vetor 2", i);
            scanf("%f", v2[i]);
        }

        for (int i = 0;i < size; i++){

            
        }

        char command;
        printf("Gostaria de rodar o programa novamente?: y/n");
        scanf(" %c", &command);
        if (command == 'y'){
            run = 1;
        }
        else{
            run = 0;
        }
    }
}