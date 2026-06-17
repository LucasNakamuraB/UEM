package com.example.restaurantebd.service;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.restaurantebd.model.*;
import com.example.restaurantebd.repository.*;
import com.example.restaurantebd.repository.PedidoRepository;

@Service
public class PedidoService {

    @Autowired
    private PedidoRepository pedidoRepository;
    
    public List<Pedido> lerPedidos(){
        return pedidoRepository.findAll();

    }
    public Pedido inserirPedido(Pedido pedido){
        return pedidoRepository.save(pedido);
    }

}
