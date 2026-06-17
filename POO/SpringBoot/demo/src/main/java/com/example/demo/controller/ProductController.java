package com.example.demo.controller;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/products")
public class ProductController {

    private double price = 0.0;

    @PostMapping("/addprice")
    public String addPrice(@RequestParam("value") double value) {
        this.price += value;
        return "OK";
    }

    @GetMapping("/getprice")
    public String getPrice() {
        return String.valueOf(this.price);
    }

    @PutMapping("/updprice")
    public String updPrice(@RequestParam("value") double value) {
        this.price = value;
        return "OK";
    }

    @DeleteMapping("/rmprice")
    public String rmPrice() {
        this.price = 0.0;
        return "OK";
    }
}
