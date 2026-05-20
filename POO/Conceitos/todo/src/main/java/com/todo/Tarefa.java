package com.todo;

public class Tarefa {
    private String descript;
    private Usuario user;

    public Tarefa(String descript, Usuario user){
        this.descript = descript;
        this.user = user;
    }

    public String getDescript(){
        return descript;
    }

    public Usuario getUser(){
        return user;
    }

    public String toString(){
        return "Tarefa: " + descript + "\nUsuario: " + user.getNome();
    }
}
