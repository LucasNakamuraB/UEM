package com.biblioteca;

public class Main{
    
    public static void main(String []args){
        Livro machadao = new Livro("D.Casmurro", "M.de Assis", 1899);

        System.out.println(machadao.toString());

        machadao.emprestar();
        machadao.emprestar();
        machadao.devolver();
        machadao.devolver();
    }
}