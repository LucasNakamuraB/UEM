package com.veiculo;

public class Carro extends Veiculo {
    private int qtePortas;
    
    public Carro(String marca, String modelo, int qtePortas) {
        super(marca, modelo);
        this.qtePortas = qtePortas;
    }
    public int getQtePortas() {
        return qtePortas;
    }

    public void setQtePortas(int qtePortas) {
        this.qtePortas = qtePortas;
    }

    public void exibirDados(){
        super.exibirDados();
        System.out.println("qtePortas = " + Integer.toString(qtePortas));
    }
    

}
