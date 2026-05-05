#include <stdio.h>
#include <stdlib.h>

void fatorial(int n, int* result){
    int x = 1;
    for (int i = i; i<= n; i++){
        x = x * i;
    }
    *result = x;
}

int* fibonacci(int n){
    int first = 0;
    int second = 1;
    int *fib;
    fib = malloc(n*sizeof(int));
    for(int i = 0;i< n;i++){
        fib[i] = first;
        int aux = first + second;
        first = second;
        second = aux;
    }
    return fib;
}

void potencia(float x, int expoente, float* result){
    float n = 1;
    for (int i = 0;i< expoente;i++){
        n = n * x;
    }
    *result = n;
}

int*  primos(int n){
    int* prim;
    int n_primos = 0;
    for (int i = 1;i <= n; i++){
        int j = 2;
        int primo = 1;
        while (j < i && primo){
            if (i%j == 0){
                primo = 0;
            }
            j ++;
        }
        if(primo){
            n_primos ++;
            int* new_prim = malloc(n_primos*sizeof(int));
            for (int k = 1;k< n_primos; k++){
                new_prim[k] = prim[k];
            }
            prim = new_prim;
            prim[n_primos-1] = i;
            prim[0] = n_primos;
            
        }
    }
    return prim;
}



void main(){
    int run = 1;
    int n = 0;
    float n2 = 0;
    int x = 0;
    int resultado = 0;
    float result_float = 0;
    while (run){
        int command = 0;
        printf("\n-- Programa --\nEscolha uma da 5 opções\n");
        printf("1 - Calcular fatorial\n");
        printf("2 - Imprimir fibbonacci\n");
        printf("3 - Calcular potencia\n");
        printf("4 - Imprimir numeros primos\n");
        printf("5 - Sair\n");
        printf("Insira o comando: ");
        scanf("%i", &command);

        switch (command)
        {
        case 1:
            printf("Insira 'n':");
            scanf("%i", &n);
            fatorial(n, &resultado);
            printf("Resultado: %i", resultado);
        break;
        case 2:
            printf("Insira o numero de casas:");
            scanf("%i", &n);
            int* fib = fibonacci(n);
            for (int i =0; i<n;i++){
                printf("%i, ", fib[i]);
            }
            free(fib);
        break;
        case 3:
            printf("Insira 'n':");
            scanf("%f", &n2);
            printf("Insira o expoente:");
            scanf("%i", &x);
            potencia(n2, x, &result_float);
            printf("Resultado: %.4f", result_float);
        break;
        case 4:
            printf("Insira a quantidade:");
            scanf("%i", &n);
            int* prim = primos(n);
            for (int i =0; i<prim[0];i++){
                printf("%i, ", prim[i]);
            }
            break;
        case 5:
            run = 0;
        break;
        
        default:
            command = 0;
            break;
        }
        
    }
}