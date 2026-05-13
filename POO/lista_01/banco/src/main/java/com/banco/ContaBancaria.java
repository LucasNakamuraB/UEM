package com.banco;

public class ContaBancaria {
    private int numero;
    private String titular;
    private float saldo;
    public int getNumero() {
        return numero;
    }
    public void setNumero(int numero) {
        this.numero = numero;
    }
    public String getTitular() {
        return titular;
    }
    public void setTitular(String titular) {
        this.titular = titular;
    }
    public float getSaldo() {
        return saldo;
    }
    public void setSaldo(float saldo) {
        this.saldo = saldo;
    }

    public void depositar(float valor){
        saldo += valor;
    }

    public void sacar(float valor){
        if (saldo >= valor){
            saldo -= valor;
        }
    }

    public float consultarSaldo(){
        return saldo;
    }
}
