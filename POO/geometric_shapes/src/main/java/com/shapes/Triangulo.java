package com.shapes;

public class Triangulo extends Shape{
    private double height;
    private double base;

    public Triangulo(double base, double height){
        super("triangulo", 3);
        this.base = base;
        this.height = height;
    }

    public double getArea(){
        return (base*height) / 2;
    }
}
