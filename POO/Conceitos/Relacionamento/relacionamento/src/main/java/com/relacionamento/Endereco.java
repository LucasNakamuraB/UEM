package com.relacionamento;

public class Endereco {
    
    private String rua;
    private int numero;
    private int cep;
    private Cidade cidade;

    public Endereco(String rua, int numero, int cep, Cidade cidade){
        this.rua = rua;
        this.numero = numero;
        this.cep = cep;
        this.cidade = cidade;
    }

    public String getRua() {
        return rua;
    }

    public int getNumero() {
        return numero;
    }

    public int getCep() {
        return cep;
    }
    public Cidade getCidade(){
        return cidade;
    }
}
