package com.livro;

public class Main {
    public static void main(String[] args) {
        ISBN isbn1 = new ISBN(123, "asdf");
        ISBN isbn2 = new ISBN(122, "qwerty");
        Livro livro1 = new Livro("1", "ninguem", isbn1);
        Livro livro2 = new Livro("2", "fds", isbn1);

        livro1.exibirDados();
        livro2.exibirDados();
        System.out.println(isbn1.getLivro().getNome());
    }
}