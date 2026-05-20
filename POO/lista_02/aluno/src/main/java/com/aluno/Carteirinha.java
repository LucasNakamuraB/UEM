package com.aluno;

public class Carteirinha {
    private int numero;
    private String emissao;

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public String getEmissao() {
        return emissao;
    }

    public void setEmissao(String emissao) {
        this.emissao = emissao;
    }

    public Carteirinha(int numero, String emissao){
        this.numero = numero;
        this.emissao = emissao;
    }

    public void exibirDados(){
        System.out.println("numero da carteirinha: " + Integer.toString(numero));
        System.out.println("data de emissao: " + emissao);
    }
    
}
