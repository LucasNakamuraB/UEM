package com.poo.restaurante_2.model;

/**
 * Request body DTO for creating a new Pedido.
 */
public class ItemRequest {
    private String item;

    // Default constructor required by frameworks like Spring/Jackson
    public ItemRequest() {}

    public ItemRequest(String item) {
        this.item = item;
    }

    public String getItem() {
        return item;
    }

    public void setItem(String item) {
        this.item = item;
    }
}