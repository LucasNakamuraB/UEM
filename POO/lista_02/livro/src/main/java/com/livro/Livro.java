package com.livro;

public class Livro {
    private String nome;
    private String autor;
    private ISBN isbn;
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getAutor() {
        return autor;
    }
    public void setAutor(String autor) {
        this.autor = autor;
    }
    public ISBN getIsbn() {
        return isbn;
    }
    public void setIsbn(ISBN isbn) {
        this.isbn = isbn;
    }
    public Livro(String nome, String autor, ISBN isbn) {
        this.nome = nome;
        this.autor = autor;
        isbn.setLivro(this);
    }

    public void exibirDados(){
        System.out.println("nome: " + nome);
        System.out.println("autor: " + autor);
        if (isbn != null){
            isbn.exibirDados();
        }
    }


}
