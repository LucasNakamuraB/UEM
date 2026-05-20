package com.zoologico;

public class Pato extends Animal implements Terrestre, Aquatico, Voador {
    public Pato(String nome){
        super(nome);
    }

    public void emitirSom(){
        System.out.println(getNome() + " fez quack");
    }

    public void andar(){
        System.out.println(getNome() + " andou");
    }
    
    public void voar(){
        System.out.println(getNome() + " voou");
     }

    public void nadar(){
        System.out.println(getNome() + " nadou");
    }
}
