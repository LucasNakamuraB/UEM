package com.mvc.view;
import java.util.Scanner;
import java.util.List;
import com.mvc.controller.TarefaControle;
import com.mvc.model.Tarefa;

public class TarefaView {
    private Scanner scan;
    private TarefaControle controle;

    public TarefaView(){
        this.controle = new TarefaControle();
        this.scan = new Scanner(System.in);
    }
    public void exibirMenu(){
        int comando;
        do{
            System.out.println("Sistem Tarefas");
            System.out.println("Digite 0, 1 ou 2:");
            comando = Integer.parseInt(scan.nextLine());

            switch (comando) {
                case 0:
                    cadastrarTarefa();
                    break;
                case 1:
                    listarTarefas();
                    break;
                
                case 2:
                    System.out.println("Programa encerrado");
                    break;
                default:
                    break;
            }
        } while(comando != 2);
    }

    private void cadastrarTarefa(){
        System.out.println("Digite o titulo");
        String titulo = scan.nextLine();
        System.out.println("Digite a descrição");
        String desc = scan.nextLine();

        controle.cadastrarTarefa(titulo, desc);
    }

    private void listarTarefas(){
        List<Tarefa> list = controle.listarTarefas();

        for(Tarefa t : list){
            System.out.println("-" + t.getTitulo());
        }
    }
}
