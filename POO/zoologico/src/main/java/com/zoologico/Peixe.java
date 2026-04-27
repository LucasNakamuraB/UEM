package com.zoologico;

public class Peixe extends Animal implements Aquatico {
    
    public Peixe(String nome){
        super(nome);
    }

    public void emitirSom(){
        System.out.println(getNome() + "fez glubglub");
    }

    public void nadar(){
        System.out.println(getNome()+ " nadou");
    }
    

}
