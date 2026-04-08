package com.calculadora;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Calculadora calculadora = new Calculadora();

        System.out.println("/---------------------------\\");
        System.out.println("|CALCULADORA DE DOIS FATORES|");
        System.out.println("\\---------------------------/");
        System.out.println("-digite 'sair' para sair-");
        String entrada = "";
        while(!entrada.equals("sair")){
            try{
            System.out.println("Digite sua expressao");
            entrada = scan.nextLine();
            String[] express = entrada.split(" ");
            if (express.length !=3){
                if (!entrada.equals("sair")){System.out.println("Expressao invalida");}
                continue;
            }

            double fator1 = Double.parseDouble(express[0]);
            calculadora.setFator1(fator1);
            String operador = express[1];
            double fator2 = Double.parseDouble(express[2]);
            calculadora.setFator2(fator2);

            double resultado = 0;
            switch (operador) {
                case "+":
                    resultado = calculadora.somar();
                    break;
                case "-":
                    resultado = calculadora.subtrair();
                    break;
                case "*":
                    resultado = calculadora.multiplicar();
                    break;
                case "/":
                    resultado = calculadora.dividir();
                    break;
                default:
                    System.out.println("Operador Invalido");
            }
            System.out.println(resultado);
            }catch(ArithmeticException e){
                System.out.println("erro:" + e);
            }
        }
        scan.close();

    }
}