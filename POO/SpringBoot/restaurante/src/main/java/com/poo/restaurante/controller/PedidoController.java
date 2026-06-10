package com.poo.restaurante.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.poo.restaurante.model.Pedido;
import com.poo.restaurante.service.PedidoService;


@RestController
@RequestMapping("/pedidos")
public class PedidoController {
    
    @Autowired
    private PedidoService pedidoService;

    @PostMapping
    public Pedido criarPedido(@RequestBody Pedido pedido){
        return pedidoService.criarPedido(pedido);
    }
    @GetMapping
    public List<Pedido> lerPedidos(){
        return pedidoService.lerListaPedido();
    }
}
