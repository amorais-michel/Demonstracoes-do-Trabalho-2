package com.mycompany.dia_da_semana;

import java.util.Scanner;

public class Dia_da_semana {

    public static void main(String[] args) {
        int numero;

        System.out.print("Digite um número");
        Scanner n = new Scanner(System.in);
        numero = n.nextInt();

        switch (numero) {
            case 1:
                System.out.println("Domingo");
                break;

            case 2:
                System.out.println("Segunda");
                break;

            case 3:
                System.out.println("Terça");
                break;

            case 4:
                System.out.println("Quarta");
                break;

            case 5:
                System.out.println("Quinta");
                break;

            case 6:
                System.out.println("Sexta");
                break;

            case 7:
                System.out.println("Sabado");
                break;

        }
        if (numero > 7) {
            System.out.print("Digite algo que corresponda a um numero da semana!");
        }

    }
}
