package com.poo.restaurante.service;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Service;

import com.poo.restaurante.model.Pedido;

@Service
public class PedidoService {
    
    private ArrayList<Pedido> pedidos = new ArrayList<>();

    public Pedido criarPedido(Pedido pedido){
        pedidos.add(pedido);
        return pedido;
    }
    public List<Pedido> lerListaPedido(){
        return pedidos;
    }
}
