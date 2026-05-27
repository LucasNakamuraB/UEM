package com.aluno;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        List<Aluno> alunos = new ArrayList<>();
        for (int i = 0; i < 3; i ++){
            alunos.add(new Aluno("Aluno" + Integer.toString(i), 15 + i));
        }
        for (int i = 0; i < 3; i ++){
            alunos.get(i).cadastrar(i, "Curso");
        }
        for (int i = 0; i < 3; i ++){
            alunos.get(i).exibirDados();
        }
        System.out.println("Remover por matricula: ");
        int rm = scan.nextInt();
        for (int i = 0; i < 3; i ++){
            if (alunos.get(i).getMatricula() == rm){
                alunos.remove(i);
            }
        }

        Pessoa[] pessoas = {null, null, null, null};
        pessoas[0] = new Aluno("asdf", 23);
        pessoas[1] = new Aluno("qwewrty", 21);
        pessoas[2] = new Professor("hgfd", 67, "uyhb", 23);
        pessoas[3] = new Professor("fghjkl", 69, "koiivguy", 1);
        for (int i = 0;i<4;i++){
            pessoas[i].exibirDados();
        }

        ArrayList<Professor> professores = new ArrayList<>();
        professores.add(new Professor("asdf", 0, "nada", 0));
        professores.add(new Professor("qwerty", 67, "coisa", 6767));
        professores.add(new Professor("joao", 88, "outra coisa", 3));
        professores.add(new Professor("zxcvb", 69, "sla", 1));
        System.out.println("Buscar professor:");
        String busca = scan.nextLine();
        Professor prof = null;
        for (int i = 0; i< professores.size();i++){
            if (busca.equals(professores.get(i).getNome())){
                prof = professores.get(i);
            }
        }
        if (prof != null){
            prof.exibirDados();
        }
        else{
            System.out.println("professor nao encontrado");
        }

    }
}