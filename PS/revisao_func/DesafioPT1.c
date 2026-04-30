#include <stdio.h>

int fatorial(int n){
    int result = 1;
    for (int i = 0; i<= n; i++){
        result = result * i;
    }
    return result;
}

void fibonacci(int n){
    int first = 0;
    int second = 1;
    while (n > 0){
        printf("%i", first);
        int aux = first + second;
        first = second;
        second = aux;
        n--;
    }
}

float potencia(float x, int expoente){
    float result = 1;
    for (int i = 0;i< expoente;i++){
        result = result * x;
    }
    return result;
}

void main(){
    int run = 1;
    while (run){
        int command = 0;
        printf("-- Programa --\nEscolha uma da 5 opções\n");
        printf("1 - Calcular fatorial\n");
        printf("2 - Imprimir fibbonacci\n");
        printf("3 - Calcular potencia\n");
        printf("4 - Imprimir numeros primos\n");
        printf("5 - Sair\n");
        scanf("Insira o comando: ", &command);

        switch (command)
        {
        case 1:
            /* code */
            break;
        case 2:
            /* code */
            break;
        case 3:
            /* code */
            break;
        case 4:
            /* code */
            break;
        case 5:
            run = 0;
            break;
        
        default:
            break;
        }
    }
}