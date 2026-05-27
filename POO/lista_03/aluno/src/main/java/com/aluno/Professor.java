package com.aluno;

public class Professor extends Pessoa {
    private String materia;
    private float salario;

    public Professor(String nome, int idade, String materia, float salario){
        super(nome, idade);
        this.materia = materia;
        this.salario = salario;
        
    }
    public String getMateria() {
        return materia;
    }
    public void setMateria(String materia) {
        this.materia = materia;
    }
    public float getSalario() {
        return salario;
    }
    public void setSalario(float salario) {
        this.salario = salario;
    }
    @Override
    public void exibirDados() {
        super.exibirDados();
        System.out.println(materia);
        System.out.println(Float.toString(salario));
    }
     
}
