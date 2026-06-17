package com.poo.restaurante_2.model;

public class Pedido {
    private Long id;
    private String item;

    // Default constructor required by frameworks like Spring/Jackson
    public Pedido() {}

    public Pedido(Long id, String item) {
        this.id = id;
        this.item = item;
    }

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getItem() {
        return item;
    }

    public void setItem(String item) {
        this.item = item;
    }
}