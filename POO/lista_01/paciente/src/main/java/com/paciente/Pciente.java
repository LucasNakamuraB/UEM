package com.paciente;

public class Pciente {
    private String nome;
    private float peso;
    private float altura;
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public float getPeso() {
        return peso;
    }
    public void setPeso(float peso) {
        this.peso = peso;
    }
    public float getAltura() {
        return altura;
    }
    public void setAltura(float altura) {
        this.altura = altura;
    }

    public void exibirFicha(){
        System.out.println("nome: " + nome);
        System.out.println("peso: " + Float.toString(peso));
        System.out.println("altura: " + Float.toString(altura));
    }

    public float calcularIMC(){
        return peso / (altura*altura);
    }

    public void classificaIMC(){
        float imc = calcularIMC();
        if (imc < 18.5){System.out.println("Baixo Peso");}
        else if (imc < 24.9){System.out.println("Normar");}
        else if (imc < 29.9){System.out.println("Sobrepeso");}
        else if (imc < 34.9){System.out.println("Obeso I");}
        else if (imc < 39.9){System.out.println("Obeso II");}
        else if (imc > 40){System.out.println("Obeso III");}

        }
    }

