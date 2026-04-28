#include <stdio.h>

void main(){
    int run = 1;
    while (run){
        int tam = 0;
        printf("insira o tamanho da sequencia de caracteres:\n");
        scanf("%i", &tam);
        char v[tam];
        for (int i = 0;i < tam; i++){
            printf("insira v[%i]: ", i);
            scanf(" %c", &v[i]);
        }
        int i = 0;
        int f = tam -1;
        int is_palindromo = 1;
        while (i < f){
            if (v[i] != v[f]){
                is_palindromo = 0;
            }
            i++;
            f--;

        }
            
        
        if (is_palindromo){
            printf("a sequencia inserida e um palindromo\n");
        }
        else{
            
            printf("\na sequencia inserida n e um palindromo\n");
        }
        printf("rodar programa novamente? y/n: ");
        char comm;
        scanf(" %c", &comm);
        if (comm == 'n'){
            run = 0;
        }
    }

}