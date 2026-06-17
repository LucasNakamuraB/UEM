package com.poo.restaurante_2.service;

import com.poo.restaurante_2.model.Pedido;
import org.springframework.stereotype.Service;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicLong;

@Service
public class PedidoService {
    // Simulating database storage with an ArrayList
    private List<Pedido> pedidos = new ArrayList<>();
    // Counter for unique IDs
    private AtomicLong idCounter = new AtomicLong(0);

    /**
     * Cria um novo pedido e o armazena na lista.
     * @param pedido O objeto Pedido completo a ser salvo.
     * @return Pedido criado com ID atribuído.
     */
    public Pedido criarPedido(Pedido pedido) {
        // Assigning a new unique ID to the incoming object and saving it
        Long newId = idCounter.incrementAndGet();
        pedido.setId(newId); // Assuming Pedido has setId method
        pedidos.add(pedido);
        return pedido;
    }

    /**
     * Busca todos os pedidos cadastrados.
     * @return Lista de pedidos.
     */
    public List<Pedido> buscarTodosPedidos() {
        // Returns a copy to prevent external modification issues
        return new ArrayList<>(pedidos);
    }

    /**
     * Busca um pedido por ID.
     * @param id O ID do pedido.
     * @return Pedido encontrado ou null se não existir.
     */
    public Pedido buscarPedidoPorId(Long id) {
        return pedidos.stream()
                .filter(p -> p.getId().equals(id))
                .findFirst()
                .orElse(null);
    }
}