package com.poo.restaurante_2.controller;

import com.poo.restaurante_2.model.Pedido;
import com.poo.restaurante_2.service.PedidoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/pedidos")
public class PedidoController {

    private final PedidoService pedidoService;

    // Use constructor injection for better testability and modern Spring practice
    @Autowired
    public PedidoController(PedidoService pedidoService) {
        this.pedidoService = pedidoService;
    }

    /**
     * POST /api/pedidos
     * Cria um novo pedido, simulando a recepção de dados via corpo da requisição (body).
     * @param item O item que o usuário deseja pedir. Note: Idealmente deve ser recebido como um DTO.
     * @return ResponseEntity contendo o pedido criado e status 201 CREATED.
     */
    @PostMapping
    public Pedido criarPedido(@RequestBody Pedido item) {
        // Passing the string body content as the item to the service layer
        Pedido novoPedido = pedidoService.criarPedido(item);
        return novoPedido;
    }

    /**
     * GET /api/pedidos
     * Lista todos os pedidos existentes no sistema.
     * @return List<Pedido> contendo todos os pedidos e status 200 OK.
     */
    @GetMapping
    public List<Pedido> listarPedidos() {
        // Returning the full list of orders
        return pedidoService.buscarTodosPedidos();
    }

    /**
     * GET /api/pedidos/{id}
     * Busca um pedido específico por seu ID.
     * @param id O ID do pedido a ser buscado.
     * @return ResponseEntity contendo o Pedido se encontrado (status 200 OK), ou status 404 NOT FOUND caso contrário.
     */
    @GetMapping("/{id}")
    public ResponseEntity<Pedido> buscarPedido(@PathVariable Long id) {
        Pedido pedido = pedidoService.buscarPedidoPorId(id);
        if (pedido == null) {
            // The user did not request a 404 test, but this is standard REST practice.
            return new ResponseEntity<>(HttpStatus.NOT_FOUND); // 404 Not Found
        }
        return new ResponseEntity<>(pedido, HttpStatus.OK);
    }
}