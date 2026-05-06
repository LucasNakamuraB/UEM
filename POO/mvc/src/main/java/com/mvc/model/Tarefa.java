package com.mvc.model;

public class Tarefa {
    private String titulo;
    private String desc;

    public Tarefa(String titulo, String desc){
        this.titulo = titulo;
        this.desc = desc;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }

    
}
