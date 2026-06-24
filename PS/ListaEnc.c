#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{
  int tipo, CPF;
  char *nome;
  float salario;
} tipoDado1;

typedef struct{
  char nome[30];
  int tipo, idade, CPF;
  char profissao[20];
} tipoDado2;

typedef struct{
  int RG, CPF;
  char nome[30], endereco[40];
  int CEP, tipo;
} tipoDado3;


typedef struct tipoNo{
    int tipoDado;
    void *pontDado;
    struct tipoNo *prox;
} tipoNo;

int criarRegistro(void** reg){
    int tipo = 1;
    switch (tipo){
        case 1:
            tipoDado1 registro;
            registro.tipo = 1;
            printf("inserir cpf:");

            scanf("%i", &(registro.CPF));
            printf("inserir nome: ");
            fgets(registro.nome, 30, stdin);
            //registro.nome = &"fodase"[0];
            registro.salario = 69;
            *reg = &registro;
        break;
        case 2:
            tipoDado2 registro2;
            *reg = &registro2;
        break;
        case 3:
            tipoDado3 registro3;
            *reg = &registro3;
        break;
    }
    return tipo;
}

tipoNo criarlista(){
    tipoNo lista;
    lista.prox = NULL;
    lista.tipoDado = criarRegistro(&(lista.pontDado));
    
    return lista;
}
void main(){
    tipoNo pinto = criarlista();
    tipoDado1 *dado;
    dado = pinto.pontDado;
    printf("%s", (*dado).nome);

}