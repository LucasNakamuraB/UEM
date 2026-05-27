package com.biblioteca;

public class LivroDidatico extends Livro {
    private String materia;

    public LivroDidatico (String titulo, String autor,String materia){
        super(titulo, autor);
        this.materia = materia;
    }

    public String getMateria() {
        return materia;
    }

    public void setMateria(String materia) {
        this.materia = materia;
    }

    public void exibirDados(){
        super.exibirDados();
        System.out.println("Materia: " + materia);
    }

}
