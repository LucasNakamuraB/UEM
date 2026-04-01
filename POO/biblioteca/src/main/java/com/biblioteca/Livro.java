package com.biblioteca;

public class Livro{

    private String titulo;
    private String autor;
    private int anoPublicacao;
    private boolean disponivel;

    public Livro(String titulo, String autor, int anoPublicacao){
        this.titulo = titulo;
        this.autor = autor;
        this.anoPublicacao = anoPublicacao;
        this.disponivel = true;
    }

    public String getTitulo(){return this.titulo;}
    public void setTitulo(String titulo){this.titulo = titulo;}
    public String getAutor(){return this.autor;}
    public void setAutor(String autor){this.autor = autor;}
    public int getAno(){return this.anoPublicacao;}
    public void setAno(int ano){this.anoPublicacao = ano;}
    public boolean isDisponivel(){return this.disponivel;}

    public void emprestar(){
        if (this.disponivel == true){
            this.disponivel = false;
            System.out.println(this.titulo + " foi emprestado com sucesso!");
        }
        else{
            System.out.println(this.titulo + " não está disponível!");
        }
    }
    public void devolver(){
        if (this.disponivel == false){
            this.disponivel = true;
            System.out.println(this.titulo + " foi devolvido com sucesso!");
        }
        else{
            System.out.println(this.titulo + " ja foi devolvido!");
        }
    }

    public String toString(){
        return "titulo: " + getTitulo() + "\n" +
            "autor: " + getAutor() + "\n"+
            "ano: " + getAno() + "\n"+
            "disponivel: " + isDisponivel() + "\n";
    }
    }
    

