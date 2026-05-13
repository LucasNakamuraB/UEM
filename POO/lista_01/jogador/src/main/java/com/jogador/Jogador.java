package com.jogador;

public class Jogador {
    private String nome;
    private int pontoacao;
    private int nivel;
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public int getPontoacao() {
        return pontoacao;
    }
    public void setPontoacao(int pontoacao) {
        this.pontoacao = pontoacao;
    }
    public int getNivel() {
        return nivel;
    }
    public void setNivel(int nivel) {
        this.nivel = nivel;
    }

    public void addPontos(int pontos){
        pontoacao += pontos;
        if (pontoacao >= 100){
            subirNivel();
        }
    }

    public void subirNivel(){
        pontoacao -= 100;
        nivel += 1;
    }

}
