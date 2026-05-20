package com.zoologico;

public class Canario extends Animal implements Voador {
     public Canario(String nome){
        super(nome);
     }

     @Override
     public void emitirSom(){
        System.out.println(getNome() + " piou");
     }

     public void voar(){
        System.out.println(getNome() + " voou");
     }

}
