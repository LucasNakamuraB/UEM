package com.funcionario;
public class Funcionario {
    private String nome;
    private String cargo;
    private float salario;
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getCargo() {
        return cargo;
    }
    public void setCargo(String cargo) {
        this.cargo = cargo;
    }
    public float getSalario() {
        return salario;
    }
    public void setSalario(float salario) {
        this.salario = salario;
    }

    public void aumentarSalario(float percentual){
        salario = salario * (1+ (percentual/100));
    }

    public void exibirFuncionario(){
        System.out.println("nome: " + nome);
        System.out.println("cargo: " + cargo);
        System.out.println("salario: " + Float.toString(salario));
    }
}
