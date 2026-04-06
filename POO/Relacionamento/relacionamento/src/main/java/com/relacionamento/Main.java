package com.relacionamento;

public class Main {
    public static void main(String[] args) {

        Cidade asdf = new Cidade("fds", "123, 312");
        Endereco fodase = new Endereco("la", 0, 0, asdf);
        Pessoa fulano = new Pessoa();
        Pessoa ciclano = new Pessoa("ciclano", 24, 321,fodase);


    }
}