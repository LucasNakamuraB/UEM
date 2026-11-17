#include "avg_filter.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define STB_IMAGE_IMPLEMENTATION
#include "libs\stb_image.h"
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "libs\stb_image_write.h"
#include <pthread.h>
#include "benchmark.h"

struct {
    unsigned char* img;
    unsigned char* new_img;
    int width;
    int height;
    int offset;
    int threads;
} typedef thread_args;

void sequential_avg(unsigned char* base, unsigned char* new, int width, int height){
    for (int i = width; i < (width) * (height -1); i ++){
        if (!(i % width == 0) && (i + 1) % width != 0){
            new[i] = get_3x3_avg(base, i, width);
        }
    }
}

void* fodase(void* arg){
    return arg;
}
void* threaded_avg(void* arg){
    thread_args* t = (thread_args*) arg;
    for (int j = t->offset + 1; j < t->height - 1; j += t->threads){
        for (int i = j * t->width + 1; i < (j + 1) * t->width - 1; i++){
            t->new_img[i] = get_3x3_avg(t->img, i, t->width);
        }
    }
    return NULL;
}

void parallel_avg(unsigned char* base, unsigned char* new, int width, int height, int threads){
    pthread_t*   tid_list = malloc(sizeof(pthread_t) * threads);
    thread_args* args     = malloc(sizeof(thread_args) * threads);

    for (int t = 0; t < threads; t++){
        args[t] = (thread_args){ base, new, width, height, t, threads };
        if (pthread_create(&tid_list[t], NULL, threaded_avg, &args[t]) != 0){
            fprintf(stderr, "pthread_create failed for thread %d\n", t);
            threads = t;   // only join the ones that started
            break;
        }
    }
    for (int t = 0; t < threads; t++){
        pthread_join(tid_list[t], NULL);
    }
    free(tid_list);
    free(args);
}

int get_3x3_avg(unsigned char* image, int position, int width){
    int sum = 0;
    int corner = position - width - 1;
    for (int i = 0; i < 3; i++){
        sum += image[corner + (i * width)] 
            + image[corner + (i * width) + 1]
            + image[corner + (i * width) + 2];
    }
    return sum / 9;
}

void main(int argc, char* argv[]){
    char* img_name = malloc(sizeof(char) * 126);
    unsigned char *img;
    int img_height, img_width, channels;
    int parallel = 0;
    int valid = 0; 
    int threads = 0;
    if (strcmp(argv[1], "-p")== 0){
        parallel = 1;
        if (argc == 4){
            valid = 1;
            strcpy(img_name, argv[2]);
            threads = atoi(argv[3]);
            printf("%i\n", threads);
        }
        else {
            printf("\n O nome do arquivo ou numero de threads não foi fornecido:\n");
            printf("    -p nome_do_arquivo numero_de_threads");
        }
    }
    else if (strcmp(argv[1], "-s") == 0){
        if (argc == 3){
            valid = 1;
            strcpy(img_name, argv[2]);
        }
        else {
            printf("\n O nome do arquivo não foi fornecido:\n");
        }
    }
    else{
        printf("\nArgumento inicial deve ser [-s | -p]");
    }
    if (valid == 1){
        start_benchmark();
        unsigned char* new_image = stbi_load(img_name, &img_width, &img_height,&channels, 1);
        img = stbi_load(img_name, &img_width, &img_height,&channels, 1);
        if (parallel == 0){
            sequential_avg(img, new_image, img_width, img_height);
        }
        else{
            parallel_avg(img, new_image, img_width, img_height, threads);
        }
        stbi_write_png("img_output\\output.png", img_width, img_height, 1, new_image, 0);
        end_benchmark();
    }
}