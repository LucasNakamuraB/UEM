package com.midia;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Midia> midias = new ArrayList<>();
        midias.add(new Filme("filme", 1));
        midias.add(new Podcast("flow", 2020));
        midias.add(new Filme("asdf", 12));
        midias.add(new Musica("sla", 2012));
        midias.add(new Musica("hmmmm", 1980));
        midias.add(new Filme("qwerty", 8));
        for (int i = 0; i< midias.size(); i ++){
            midias.get(i).exibirDados();
        }
        System.out.println("\n filmes:");
        for (int i = 0; i< midias.size(); i ++){
            if (midias.get(i) instanceof Filme){
                midias.get(i).exibirDados();
            }
        }
        int filmes = 0;
        int musicas = 0;
        int pods = 0;
        for (int i = 0; i< midias.size(); i ++){
            if (midias.get(i) instanceof Filme){
                filmes ++;
            }
            if (midias.get(i) instanceof Musica){
                musicas++;
            }
            if (midias.get(i) instanceof Podcast){
                pods++;
            }
        }
        System.out.println("n filmes: "+ Integer.toString(filmes));
        System.out.println("n musicas: "+ Integer.toString(musicas));
        System.out.println("n podcasts: "+ Integer.toString(pods));

    }
}