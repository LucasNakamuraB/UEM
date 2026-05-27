package com.veiculo;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Boolean run = true;
        ArrayList<Veiculo> armazenamento = new ArrayList<>();
        while (run){
            System.out.println("Sistema de veiculos, digite:");
            System.out.println("1 para adicionar veiculo");
            System.out.println("2 para remover veiculo");
            System.out.println("3 para buscar veiculo");
            System.out.println("4 para exibir veiculos");
            System.out.println("0 para sair");
            int command = Integer.parseInt(scan.nextLine());
            switch (command){
                case 1:
                    System.out.println("carro 1 ou moto 2");
                    command = Integer.parseInt(scan.nextLine());
                    if (command == 1){
                        System.out.println("Marca");
                        String marca = scan.nextLine();
                        System.out.println("Modelo");
                        String modelo = scan.nextLine();
                        System.out.println("Qte de Portas");
                        int qte = scan.nextInt();
                        scan.nextLine();
                        armazenamento.add(new Carro(marca, modelo, qte));
                    }
                    else if (command == 2){
                        System.out.println("Marca");
                        String marca = scan.nextLine();
                        System.out.println("Modelo");
                        String modelo = scan.nextLine();
                        System.out.println("Cilindradas");
                        int qte = scan.nextInt();
                        scan.nextLine();
                        armazenamento.add(new Moto(marca, modelo, qte));
                    }
                break;
                case 2:
                    System.out.println("insira modelo");
                    String modelo = scan.nextLine();
                    for (int i = 0;i< armazenamento.size(); i++){
                        if (modelo.equals(armazenamento.get(i).getModelo())){
                            armazenamento.remove(i);
                        }
                    }
                break;
                case 3:
                    System.out.println("insira modelo");
                    String model = scan.nextLine();
                    for (int i = 0;i< armazenamento.size(); i++){
                        if (model.equals(armazenamento.get(i).getModelo())){
                            armazenamento.get(i).exibirDados();
                        }
                    }
                break;
                case 4:
                    System.out.println(armazenamento.toString());
                break;
                case 0:
                    run = false;
                break;
            }
        }


        /*Carro[] carros = {null, null, null, null};
        for (int i = 0; i< 4; i++){
            System.out.println("carro " + Integer.toString( + 1));
            System.out.println("Marca");
            String marca = scan.nextLine();
            System.out.println("Modelo");
            String modelo = scan.nextLine();
            System.out.println("Qte de Portas");
            int qte = scan.nextInt();
            scan.nextLine();
            carros[i] = new Carro(marca, modelo, qte);
        }
        for (int i = 0; i< 4; i++){
            carros[i].exibirDados();
        }

        //EX 23

        ArrayList<Carro> carros_list = new ArrayList<>();
        for (int i = 0; i< 4; i++){
            System.out.println("carro " + Integer.toString( + 1));
            System.out.println("Marca");
            String marca = scan.nextLine();
            System.out.println("Modelo");
            String modelo = scan.nextLine();
            System.out.println("Qte de Portas");
            int qte = scan.nextInt();
            scan.nextLine();
            carros_list.add(new Carro(marca, modelo, qte));
        }
        System.out.println(carros_list.toString());
        //Mais flexivel e mais facil de printar */
    }
}