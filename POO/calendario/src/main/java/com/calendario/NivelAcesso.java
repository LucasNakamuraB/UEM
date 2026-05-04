package com.calendario;

public enum NivelAcesso {
    ADMIN("foda"),
    USUARIO("ok"),
    LEITOR("plebe");

    private String descrit;

    NivelAcesso(String descrit){
        this.descrit = descrit;
    }

    public String getDescrit(){
        return descrit;
    }
}
