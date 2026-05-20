package com.shapes;

public class Square extends Shape{

    private double size;

    public Square(double size){
        super("square", 4);
        this.size = size;
    }

    @Override
    public double getArea(){
        return size * size;
    }

}