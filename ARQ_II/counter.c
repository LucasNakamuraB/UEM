#include <pthread.h>
#include "benchmark.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

pthread_mutex_t count_mutex;
int threads = 0;

void show_args(int parallel, int valid, int thread_n){
    printf("parallel=%i\n", parallel);
    printf("valid=%i\n", valid);
    printf("threads=%i\n", thread_n);
}

void seq_count(){
    int* var = malloc(sizeof(int));
    *var = 0;
    while (*var != 100000000)
    {
        (*var )++;
    }
    
}

void* threaded_count_mutex(void* arg){
    int* var = (int*) arg;
    pthread_mutex_lock(&count_mutex);
    while (*var != 100000000) {
        (*var)++;
        pthread_mutex_unlock(&count_mutex);
    }
    pthread_mutex_unlock(&count_mutex);
    
    return NULL;
}

void* threaded_count(void* arg){
    int* var = (int*) arg;
    int i = 0;
    while (i != 25000000) {
        i++;
    }
    *var += i;
    return NULL;
}

void run_parallel_count(){
    pthread_t* tid_list = malloc(sizeof(pthread_t) * threads);
    int* var = malloc(sizeof(int));
    *var = 0;

    for (int i = 0; i < threads; i++){
        pthread_create(&tid_list[i], NULL, threaded_count, var);
    }
    
    for (int i = 0; i < threads; i++){
        pthread_join(tid_list[i], NULL);
    }
    printf("%i", *var);
    free(var);
}

void run_parallel_count_mutex(){
    pthread_t* tid_list = malloc(sizeof(pthread_t) * threads);
    int* var = malloc(sizeof(int));
    *var = 0;

    for (int i = 0; i < threads; i++){
        printf("thread created\n");
        pthread_create(&tid_list[i], NULL, threaded_count_mutex, var);
    }
    
    for (int i = 0; i < threads; i++){
        pthread_join(tid_list[i], NULL);
        printf("thread joined\n");
    }
    printf("%i", *var);
    free(var);
}


void main(int argc, char* argv[]){
    int valid = 0;
    int parallel = 0;

    pthread_mutex_init(&count_mutex, NULL);

    if (!strcmp(argv[1], "-p")){
        parallel = 1;
        if (argc >= 3){
            valid = 1;
            threads = atoi(argv[2]);
        }
    }
    else if (!strcmp(argv[1], "-s")){
        valid = 1;
    }
    show_args(parallel, valid, threads);

    if (valid){
        start_benchmark();
        if (parallel){
            if (argc == 4 && !strcmp(argv[3], "-m")){
                run_parallel_count_mutex();
            }
            else{run_parallel_count();}
        }
        else{
            seq_count();
        }
    }
    else{
        printf("argumentos invalidos");
    }
    end_benchmark();
    
    pthread_mutex_destroy(&count_mutex);
}