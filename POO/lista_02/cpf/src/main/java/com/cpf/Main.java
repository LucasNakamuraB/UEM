package com.cpf;

public class Main {
    public static void main(String[] args) {
        Cpf cepeefe = new Cpf(123123123, "regular");
        Pessoa jao = new Pessoa("jao", 67, cepeefe);

        jao.exibirDados();
    }
}