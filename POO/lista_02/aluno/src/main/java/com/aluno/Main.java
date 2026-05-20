package com.aluno;

public class Main {
    public static void main(String[] args) {
        Carteirinha carteirinha = new Carteirinha(67, "6\7\1967");
        Aluno aluno = new Aluno ("aluno", "curso", carteirinha);

        aluno.exibirDados();
    }
}