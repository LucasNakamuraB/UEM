package com.midia;

public class Midia {
    public String titulo;
    public int ano;

    public Midia(String titulo, int ano){
        this.titulo = titulo;
        this.ano = ano;
    }

    public String getTitulo() {
        return titulo;
    }
    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }
    public int getAno() {
        return ano;
    }
    public void setAno(int ano) {
        this.ano = ano;
    }

    public void exibirDados(){
        System.out.println("titulo: " + titulo);
        System.out.println("ano: " + Integer.toString(ano));
    }
}
