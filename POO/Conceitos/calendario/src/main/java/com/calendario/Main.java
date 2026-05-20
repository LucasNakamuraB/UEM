package com.calendario;

public class Main {

    public static void main(String[] args) {
        Atividade ativ = new Atividade("Comer c* de curioso", "06:07", DiaSemana.SEXTA);
        System.out.println("preciso " + ativ.getAtividade() + " as " + ativ.getHora() + " de " + ativ.getDia().getNome());
        
    }

}