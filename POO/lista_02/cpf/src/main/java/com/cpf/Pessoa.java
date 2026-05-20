package com.cpf;

public class Pessoa {
    private String nome;
    private int  idade;
    private Cpf cpf;
    
    public Pessoa(String nome, int idade,Cpf cpf){
        this.nome = nome;
        this.idade = idade;
        this.cpf = cpf;
    }
    
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public int getIdade() {
        return idade;
    }
    public void setIdade(int idade) {
        this.idade = idade;
    }
    public Cpf getCpf() {
        return cpf;
    }
    public void setCpf(Cpf cpf) {
        this.cpf = cpf;
    }

    public void exibirDados(){
        System.out.println("nome: " + nome);
        System.out.println("idade: " + idade);
        cpf.exibirDados();
    }
}
