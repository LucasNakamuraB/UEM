package com.shapes;

public abstract class Shape {
    
    private String name;
    private int n_sides;

    public Shape(String name, int n_sides){
        this.name = name;
        this.n_sides = n_sides;
    }

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name = name;
    }

    public int getNSides(){
        return n_sides;

    }

    public void setNSides(int n_sides){
        this.n_sides = n_sides;
    }

    public abstract double getArea();
}
