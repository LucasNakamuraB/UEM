package com.calendario;

public enum DiaSemana {
    SEGUNDA("segunda-feira"),
    TERCA("terça-feira"),
    QUARTA("quarta-feira"),
    QUINTA("quinta-feira"),
    SEXTA("sexta-feira"),
    SABADO("sábado"),
    DOMINGO("domingo");

    private String nome;

    DiaSemana(String nome){
        this.nome = nome;
    }

    public String getNome(){
        return nome;
    }
}
