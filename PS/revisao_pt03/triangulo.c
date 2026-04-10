#include <stdio.h>

void main(void){
    int size = 0;
    printf("tamanho: ");
    scanf("%i", &size);
    int axis = size/2;
    for (int dots = 1; dots <= size;dots += 2){
        int i = 0;
        while (i<axis){
            printf(" ");
            i++;
        }
        i = 0;
        while(i< dots){
            i++;
            printf("*");
        }
        printf("\n");
        axis -= 1;
    }
}