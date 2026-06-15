package com.example.restaurantebd.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;

@Entity
public class Pedido {

    @Id
    private int id;
    private String nome;

    public int getId() {
        return id;
    }
    public String getNome() {
        return nome;
    }


}
