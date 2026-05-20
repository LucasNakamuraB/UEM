package com.relacionamento;

public class Main {
    public static void main(String[] args) {

        Cidade cidade_buxa = new Cidade("fds", "123, 312");
        Endereco fodase = new Endereco("la", 0, 0, cidade_buxa);
        Pessoa fulano = new Pessoa();
        Pessoa ciclano = new Pessoa("ciclano", 24, 321,fodase);
        System.out.println(ciclano.getNome());
        System.out.println(fulano.getNome());


    }
}