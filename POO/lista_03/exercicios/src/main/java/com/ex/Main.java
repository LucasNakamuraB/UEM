package com.ex;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        //EX 22
        int[] seisnumeros = {0, 0, 0, 0, 0, 0};
        for (int i = 0; i < 6; i++){
            System.out.println("Digite numero " + Integer.toString(1+i) + "\6");
            seisnumeros[i] = scan.nextInt();
        }
        for (int i = 0;i<seisnumeros.length;i++){
            System.out.print(Integer.toString(seisnumeros[i]) + "' ");
        }
        //Array usado para um numero fixo de elementos, mais dificil de imprimir

        ArrayList<Integer> numeros = new ArrayList<>();
        System.out.println("Digite um numero, ou nada para finalizar");
        scan.nextLine();
        String n_str = scan.nextLine();
        while (!n_str.equals("")){
            numeros.add(Integer.parseInt(n_str));
            System.out.println("Digite um numero, ou nada para finalizar");
            //scan.nextLine();
            n_str = scan.nextLine();
        }
        System.out.println(numeros.toString());
        //mais flexivel e facil de imprimir

        //EX 23 e 24 em veiculos
        //EX 25:
        /*
        a) O que é herança?
        a possibilidade de uma subclasse de herdar atributos e funcoes de uma superclasse
        b) Qual a diferença entre classe base e subclasse?
        a classe base e relativamente independente, a subclasse deriva da classe base
        c) O que é um array?
        uma arranjo de tamanho fixo de um determinado tipo de dado
        d) O que é um ArrayList?
        uma estrutura de um detarminado tipo de dados com tamanho variavel e acesso aleatorio
        e) Qual a principal diferença entre array e ArrayList?
        o array e fixo, ArrayList varia de tamanho
        f) Por que uma ArrayList<Pessoa> pode armazenar Aluno e Professor?
        pois aluno e professor sao ambos subclasses de pessoa
        */


    }
}