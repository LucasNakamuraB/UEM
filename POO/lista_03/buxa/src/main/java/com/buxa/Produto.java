package com.buxa;

public class Produto {
    private String nome;
    private float preco;

    public Produto(String nome, float preco){
        this.nome = nome;
        this.preco = preco;
    }

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public float getPreco() {
        return preco;
    }
    public void setPreco(float preco) {
        this.preco = preco;
    }

    public void exibirDados(){
        System.out.println("produto: " + nome);
        System.out.println("preco: " + Float.toString(preco));
    }

    
}
