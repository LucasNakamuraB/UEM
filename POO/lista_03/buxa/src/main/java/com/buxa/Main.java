package com.buxa;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        /*ArrayList<Integer> vec = new ArrayList<Integer>();
        for (int i = 0; i < 5; i++){
            int num = scan.nextInt();
            vec.add(num);
        }
        System.out.println(vec.toString());
        int soma = 0;
        for (int i = 0; i < 5; i++){
            soma += vec.get(i);
        }
        System.out.println(Integer.toString(soma)); */

        ArrayList<String> nomes = new ArrayList<>();
        for (int i = 0; i < 5; i++){
            nomes.add(Integer.toString(i));
        }
        System.out.println(nomes.toString());
        System.out.println("Quantidade cadastrada = " + Integer.toString(nomes.size()));

        ArrayList<Produto> produtos = new ArrayList<>();
        for (int i = 0;i < 5;i ++){
            produtos.add(new Produto("nome", i * 5));
        }
        for (int i = 0;i < 5;i ++){
            produtos.get(i).exibirDados();
        }
        Produto maior = produtos.get(0);
        for (int i = 0;i < 5;i ++){
            if (produtos.get(i).getPreco() > maior.getPreco()){
                maior = produtos.get(i);
            }
        }
        System.out.println("Maior Preco:");
        maior.exibirDados();

        scan.close();

    }
}