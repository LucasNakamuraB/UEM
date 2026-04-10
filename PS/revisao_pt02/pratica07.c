#include <stdio.h>

void main(){
    int num1 = 0;
    int num2 = 0;
    int num3 = 0;
    int num4 = 0;
    
    printf("Insira o numero 1:");
    scanf("%i", &num1);
    printf("\nInsira o numero 2:");
    scanf("%i", &num2);
    printf("\nInsira o numero 3:");
    scanf("%i", &num3);
    printf("\nInsira o numero 4:");
    scanf("%i", &num4);
    
    if (num1<num2&&num2<num3&&num3<num4){printf("%i, %i, %i, %i",num1,num2,num3,num4);}
    else if (num1<num2&&num2<num4&&num4<num3){printf("%i, %i, %i, %i",num1,num2,num4,num3);}
    else if (num1<num4&&num4<num2&&num2<num3){printf("%i, %i, %i, %i",num1,num4,num2,num3);}
    else if (num1<num4&&num4<num3&&num3<num2){printf("%i, %i, %i, %i",num1,num4,num2,num3);}
    else if (num1<num3&&num3<num2&&num2<num4){printf("%i, %i, %i, %i",num1,num3,num2,num4);}
    else if (num1<num3&&num3<num4&&num4<num2){printf("%i, %i, %i, %i",num1,num3,num4,num2);}
    else if (num2<num1&&num1<num3&&num3<num4){printf("%i, %i, %i, %i",num2,num1,num3,num4);}
    else if (num2<num1&&num1<num4&&num4<num3){printf("%i, %i, %i, %i",num2,num1,num4,num3);}
    else if (num2<num3&&num3<num1&&num1<num4){printf("%i, %i, %i, %i",num2,num3,num1,num4);}
    else if (num2<num3&&num3<num4&&num4<num1){printf("%i, %i, %i, %i",num2,num3,num4,num1);}
    else if (num2<num4&&num4<num1&&num1<num3){printf("%i, %i, %i, %i",num2,num4,num1,num3);}
    else if (num2<num4&&num3<num3&&num3<num1){printf("%i, %i, %i, %i",num2,num4,num4,num1);}
    else if (num3<num1&&num1<num2&&num2<num4){printf("%i, %i, %i, %i",num3,num1,num2,num4);}
    else if (num3<num1&&num1<num4&&num4<num2){printf("%i, %i, %i, %i",num3,num1,num4,num2);}
    else if (num3<num2&&num2<num1&&num1<num4){printf("%i, %i, %i, %i",num3,num2,num1,num4);}
    else if (num3<num2&&num2<num4&&num4<num1){printf("%i, %i, %i, %i",num3,num2,num4,num1);}
    else if (num3<num4&&num4<num1&&num1<num2){printf("%i, %i, %i, %i",num3,num4,num1,num2);}
    else if (num3<num4&&num4<num2&&num2<num1){printf("%i, %i, %i, %i",num3,num4,num2,num1);}
    else if (num4<num1&&num1<num2&&num2<num3){printf("%i, %i, %i, %i",num4,num1,num2,num3);}
    else if (num4<num1&&num1<num3&&num3<num2){printf("%i, %i, %i, %i",num4,num1,num3,num2);}
    else if (num4<num2&&num2<num1&&num1<num3){printf("%i, %i, %i, %i",num4,num2,num1,num3);}
    else if (num4<num2&&num2<num3&&num3<num1){printf("%i, %i, %i, %i",num4,num2,num3,num1);}
    else if (num4<num3&&num3<num1&&num1<num2){printf("%i, %i, %i, %i",num4,num3,num1,num2);}
    else if (num4<num3&&num3<num2&&num2<num1){printf("%i, %i, %i, %i",num4,num3,num2,num1);}

}
