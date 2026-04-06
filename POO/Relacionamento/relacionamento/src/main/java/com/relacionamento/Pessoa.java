package com.relacionamento;

public class Pessoa{

    private String nome;
    private int cpf;
    private int idade;
    private Endereco endereco;

    public Pessoa(){}

    public Pessoa(String nome, int idade, int cpf, Endereco endereco){
        this.nome = nome;
        this.idade = idade;
        this.cpf = cpf;
        this.endereco = endereco;
    }

    public String getNome(){return this.nome;}
    public void setNome(String nome){this.nome = nome;}

    public int getIdade(){return this.idade;}
    public void setIdade(int idade){this.idade = idade;}

    public int getCpf(){return this.cpf;}
    public void setCpf(int cpf){this.cpf = cpf;}

    public Endereco getEndereco(){return this.endereco;}
    public void setEndereco(Endereco endereco){this.endereco = endereco;

    }

}