package com.calculadora;

public class Calculadora {
    
    private double fator1, fator2;

    public void setFator1(double fator){fator1 = fator;}
    public double getFator1(double fator){return fator1;}
    public void setFator2(double fator){fator2 = fator;}
    public double getFator2(double fator){return fator2;}

    public double somar(){
        return fator1 + fator2;
    }
    public double subtrair(){
        return fator1 - fator2;
    }
    public double multiplicar(){
        return fator1 * fator2;
    }
    public double dividir(){
        if (fator2 == 0){
            throw new ArithmeticException("Divisao por 0");
        }
        return fator1 / fator2;
    }
}
