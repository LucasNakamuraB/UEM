#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include "mult_matriz.h"
#include "benchmark.h"

int size, threads = 0;

matrix create_matrix(int size){
    matrix mat = malloc(sizeof(int*) * size);
    for (int i = 0; i< size; i++){
        mat[i] = malloc(sizeof(int) * size);
    }
    return mat;
}

void print_matrix(char* name, matrix mat, int size){
    printf("\nNome: %s \n", name);
    for (int k = 0;k < size; k++){
        printf("|");
        for (int l = 0; l<size; l++){
            printf("%i ", mat[k][l]);
        }
        printf("|\n");
    }

}

matrix read_matrix(int size, char *filename){
    FILE* file = fopen(filename, "r");
    char* buffer;
    matrix mat = create_matrix(size);
    for (int i = 0; i<size; i++){
        for (int j = 0; j<size; j++){
            fscanf(file,"%i", &mat[i][j]);
        }
    }
    return mat;
}

int mult_line_row(int* line, matrix mat, int row, int size){
    int sum = 0;
    for (int i =0; i < size; i++){
        sum += line[i] * mat[i][row];
    }
    return sum;
}

int* multiply_line(int* line, matrix mat, int size){
    int *new_line = malloc(sizeof(int) * size);
    for (int i = 0; i < size; i++){
        new_line[i] = mult_line_row(line, mat, i, size);
    }
    return new_line;
}



matrix sequential_mult(matrix a, matrix b, int size){
    matrix ab = malloc(sizeof(int*) * size);
    for (int i = 0; i< size; i++){
        ab[i] = multiply_line(a[i], b, size);
    }
    return ab;
}

typedef struct{
    matrix ab;
    matrix a;
    matrix b;
    int offset;
} thread_arg;

void* thread_multiply(void* args){
    thread_arg arg = *(thread_arg*)args;
    for (int i = arg.offset; i < size; i += threads){
        arg.ab[i] = multiply_line(arg.a[i], arg.b, size);
    }
}

matrix parallel_multiply(matrix a, matrix b,int threads, int size){
    pthread_t *tid_list = malloc(sizeof(pthread_t) * threads);
    matrix ab = malloc(sizeof(int*) * size);
    for (int i = 0; i < threads; i++){
        thread_arg arg;
        arg.a = a;
        arg.b = b;
        arg.ab = ab;
        arg.offset = i;
        pthread_create(&tid_list[i], NULL, thread_multiply, &arg);
    }
    for (int i =0; i< threads; i ++){
        pthread_join(tid_list[i], NULL);
        printf("a thread joined\n");
    }
    free(tid_list);
    return ab;
}

void main(int argc, char *argv[]){
    char* a_name = malloc(sizeof(char) * 64);
    char* b_name = malloc(sizeof(char) * 64);
    int paralel, valid = 0;
    if (strcmp(argv[1], "-p") == 0){
        paralel = 1;
        if (argc != 6) {
            printf("Argumentos invalidos, deve conter:\n");
            printf("    -p sua_matriz.txt outra_matriz.txt n_treads ordem_matriz");
        }
        else{
            valid = 1;
            strcpy(a_name, argv[2]);
            strcpy(b_name, argv[3]);
            threads = atoi(argv[4]);
            size = atoi(argv[5]);
            printf("%s, %s, %i, %i", a_name, b_name, threads, size);
        }
    }
    else if (strcmp(argv[1], "-s") == 0){
        paralel = 0;
        printf("%s", argv[4]);
        if (argc != 5) {
            printf("Argumentos invalidos, deve conter:\n");
            printf("    -s sua_matriz.txt outra_matriz.txt ordem_matriz");
        }
        else{
            valid = 1;
            strcpy(a_name, argv[2]);
            strcpy(b_name, argv[3]);
            size = atoi(argv[4]);
            printf("%s, %s, %i", a_name, b_name, size);
        }
    }
    else{
        printf("Argumento inicial deve ser [-s | -p]");
    }
    if (valid){
        matrix a_matrix = read_matrix(size, a_name);
        matrix b_matrix = read_matrix(size, b_name);
        matrix ab;
        
        start_benchmark();
        if (!threads){
            
            ab = sequential_mult(a_matrix, b_matrix, size);
            end_benchmark();
        }
        else{
            
            ab = parallel_multiply(a_matrix, b_matrix, threads, size);
            end_benchmark();
        }
        //print_matrix("Matriz AxB", ab, size);
    }
    
}
