package com.livro;

public class ISBN {
    private int codigo;
    private String editora;
    private Livro livro;

    public Livro getLivro() {
        return livro;
    }

    public void setLivro(Livro livro) {
        if (this.livro == null){
            this.livro = livro;
            livro.setIsbn(this);
        }
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public String getEditora() {
        return editora;
    }

    public void setEditora(String editora) {
        this.editora = editora;
    }

    public ISBN(int codigo, String editora){
        this.codigo = codigo;
        this.editora = editora;
        this.livro = null;
    }

    public void exibirDados(){
        System.out.println("codigo: " + Integer.toString(codigo));
        System.out.println("editora: " + editora);
    }
}
