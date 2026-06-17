package com.example.restaurantebd.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.restaurantebd.service.*;
import com.example.restaurantebd.service.PedidoService;
import com.example.restaurantebd.model.*;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;


@RestController
@RequestMapping("/pedidos")
public class PedidoController {

    @Autowired
    private PedidoService pedidoService;
    
    public List<Pedido> pedidos;

    @GetMapping
    public List<Pedido> lerPedidos(){
        return pedidoService.lerPedidos();
    }
    @PostMapping
    public Pedido inserirPedido(@RequestBody Pedido pedido){
        return pedidoService.inserirPedido(pedido);
    }
    
}
