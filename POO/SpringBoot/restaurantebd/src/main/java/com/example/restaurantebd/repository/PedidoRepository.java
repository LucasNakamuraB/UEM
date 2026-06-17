package com.example.restaurantebd.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.example.restaurantebd.model.*;;


public interface PedidoRepository extends JpaRepository<Pedido, Integer>{
    
}
