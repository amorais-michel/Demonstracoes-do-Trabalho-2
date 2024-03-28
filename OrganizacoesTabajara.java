package com.mycompany.organizacoestabajara;

import java.util.Scanner;


public class OrganizacoesTabajara {

    public static void main(String[] args) {
        
        
        double aumento,novo_salario ;
       
       
        // Pedindo o salario do usuario
        
        Scanner s = new Scanner(System.in);
        System.out.printf("Salario:");
        float salario_inicial = s.nextFloat();
        
        if (salario_inicial <= 280.00){
           
           System.out.println("Voce tem direito a 20% de aumento!");
           
           aumento = (salario_inicial * 0.20);
           System.out.println("Valor do aumento:" + aumento);
           
           System.out.println("Salario antes do ajuste:" + salario_inicial);
           
           novo_salario = aumento + salario_inicial;
           System.out.println("Salario com ajuste:" + novo_salario);
           
           
        }
        else if(salario_inicial == 280.01 || salario_inicial <= 700.00){
           System.out.println("Voce tem direito a 15% de aumento!");
           
           aumento = (salario_inicial * 0.15);
           System.out.println("Valor do aumento:" + aumento);
           
           System.out.println("Salario antes do ajuste:" + salario_inicial);
           
           novo_salario = aumento + salario_inicial;
           System.out.println("Salario com ajuste:" + novo_salario);
        }
        
        else if(salario_inicial == 700.01 || salario_inicial <= 1500.00){
           System.out.println("Voce tem direito a 10% de aumento!");
           
           aumento = (salario_inicial * 0.10);
           System.out.println("Valor do aumento:" + aumento);
           
           System.out.println("Salario antes do ajuste:" + salario_inicial);
           
           novo_salario = aumento + salario_inicial;
           System.out.println("Salario com ajuste:" + novo_salario);
        }
         else if(salario_inicial >= 1500){
           System.out.println("Voce tem direito a 5% de aumento!");
           
           aumento = (salario_inicial * 0.5);
           System.out.println("Valor do aumento:" + aumento);
           
           System.out.println("Salario antes do ajuste:" + salario_inicial);
           
           novo_salario = aumento + salario_inicial;
           System.out.println("Salario com ajuste:" + novo_salario);
        }
    }
}
