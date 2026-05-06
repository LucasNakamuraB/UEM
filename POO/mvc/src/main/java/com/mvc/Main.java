package com.mvc;

import com.mvc.view.TarefaView;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        TarefaView tview = new TarefaView();
        tview.exibirMenu();
    }
}