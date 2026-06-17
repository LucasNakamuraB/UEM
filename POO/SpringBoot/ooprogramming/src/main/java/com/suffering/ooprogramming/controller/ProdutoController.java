package com.suffering.ooprogramming.controller;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/")
public class ProdutoController {

    @PostMapping
    public String addOrcamento(){
        return "orcamento added";
    }

    @GetMapping
    public String getOrcamento(){
        return "orcamento read";
    }

    @PutMapping
    public String altOrcamento(){
        return "orcamento modified";
    }

    @DeleteMapping
    public String rmOrcamento(){
        return "orcamento removed";
    }
    
}
