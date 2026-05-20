package com.mvc.controller;
import java.util.ArrayList;
import java.util.List;
import com.mvc.model.Tarefa;;

public class TarefaControle {
    private List<Tarefa> tarefas;
    
public TarefaControle(){
    tarefas = new ArrayList<Tarefa>();
}

    public boolean cadastrarTarefa(String titulo, String desc){
        if (titulo == null || titulo.isBlank()){
            return false;
        }
        Tarefa tr1 = new Tarefa(titulo, desc);
        tarefas.add(tr1);
        return true;
    }

    public List<Tarefa> listarTarefas(){
        return tarefas;
    }
}
