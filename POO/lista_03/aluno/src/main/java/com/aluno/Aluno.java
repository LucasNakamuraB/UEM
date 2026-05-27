package com.aluno;

public class Aluno extends Pessoa {
    private int matricula;
    private String curso;

    public Aluno(String nome, int idade){
        super(nome, idade);
    }

    public void cadastrar(int matricula, String curso){
        this.matricula = matricula;
        this.curso = curso;
    }

    public int getMatricula() {
        return matricula;
    }
    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }
    public String getCurso() {
        return curso;
    }
    public void setCurso(String curso) {
        this.curso = curso;
    }

    public void exibirDados(){
        super.exibirDados();
        System.out.println("matricula: " + Integer.toString(matricula));
        System.out.println("curso: " + curso);
    }
    
    

}
