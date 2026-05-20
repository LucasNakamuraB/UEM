package com.relacionamento;

public class Cidade{

    private String nome;
    private String coordenadas;
    
    public Cidade(){}
    
    public Cidade(String nome, String coordenadas){
        this.nome = nome;
        this.coordenadas = coordenadas;
    }

    public String getNome() {
        return nome;
    }

    public String getCoordenadas() {
        return coordenadas;
    }

}