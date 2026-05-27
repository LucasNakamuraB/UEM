package com.biblioteca;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Livro dcasmurro = new Livro("dom casmurro", "machado");
        Livro cthulhu = new Livro("call of cthulhu", "lovecraft");
        Livro fds = new Livro("aquele la", "alguem");
        Livro[] livros_array = {dcasmurro, cthulhu, fds};
        LivroDidatico poo = new LivroDidatico("Programacao objetos", "o proprio capeta", "poo");
        LivroDidatico calculo = new LivroDidatico("calculo 2", "demonio", "calculo 2");

        ArrayList<Livro> livros_list = new ArrayList<>();
        livros_list.add(poo);
        livros_list.add(calculo);
        for (int i = 0; i< livros_array.length; i++){
            livros_array[i].exibirDados();
        }
        for (int i = 0; i<livros_list.size();i++){
            livros_list.get(i).exibirDados();
        }
    }
}