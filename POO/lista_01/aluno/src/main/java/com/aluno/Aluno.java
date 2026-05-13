package com.aluno;

public class Aluno {
    private String nome;
    private int matricula;
    private float nota1;
    private float nota2;
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public int getMatricula() {
        return matricula;
    }
    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }
    public float getNota1() {
        return nota1;
    }
    public void setNota1(float nota1) {
        this.nota1 = nota1;
    }
    public float getNota2() {
        return nota2;
    }
    public void setNota2(float nota2) {
        this.nota2 = nota2;
    }

    public float calcularMedia(){
        return (nota1 + nota2) / 2;
    }

    public boolean verificarSituacao(){
        if (calcularMedia() < 70){
            return false;
        }
        else{
            return true;
        }
    }

}
