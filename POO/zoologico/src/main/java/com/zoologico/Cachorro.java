package com.zoologico;

public class Cachorro extends Animal {

    public Cachorro(String nome){
        super(nome);
    }

    @Override
    public void emitirSom(){
        System.out.println(getNome() + " latiu");
    }

    public void andar(){
        System.out.println(getNome() + " andou");
    }
}
