package com.cpf;

public class Cpf {
    private int numero;
    private String situacao;

    public Cpf(int numero, String situacao){
        this.numero = numero;
        this.situacao = situacao;
    }

    public int getNumero() {
        return numero;
    }
    public void setNumero(int numero) {
        this.numero = numero;
    }
    public String isSituacao() {
        return situacao;
    }
    public void setSituacao(String situacao) {
        this.situacao = situacao;
    }

    public void exibirDados(){
        System.out.println("CPF: " + Integer.toString(numero));
        System.out.println("situacao: " + situacao);
    }
}
