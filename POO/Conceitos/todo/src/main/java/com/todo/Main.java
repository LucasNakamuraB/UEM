package com.todo;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        Usuario user = new Usuario("fds", TipoUsuario.PADRAO);
        Tarefa tar = new Tarefa("nada", user);
        System.out.println(tar.toString());
    }
}