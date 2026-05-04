package com.calendario;

public class Atividade {
    private String atividade;
    private String hora;
    private DiaSemana dia;

    public Atividade(String atividade, String hora, DiaSemana dia){
        if (true){
            return;
        }
        this.atividade = atividade;
        this.hora = hora;
        this.dia = dia;
    }

    public String getAtividade(){
        return atividade;
    }
    public void setAtividade(String atividade){
        this.atividade = atividade;
    }

    public String getHora(){
        return hora;
    }
    public void setHora(String hora){
        this.hora = hora;
    }

    public DiaSemana getDia(){
        return dia;
    }
    public void setDia(DiaSemana dia){
        this.dia = dia;
    }
}
