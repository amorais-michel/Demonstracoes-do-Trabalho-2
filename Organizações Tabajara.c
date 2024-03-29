#include <stdio.h>
int main(){
	
	float salario_inicial, salario_aumentado, aumento;
	
	printf("Salario em digitos:");
	scanf("%f",&salario_inicial);

	if (salario_inicial <= 280.00) {
		printf("\nTem direito a um aumento de 20 porcento");
		
		printf("\nSeu salario anterior e de: R$:%2.f", salario_inicial );
		
		aumento =  ( salario_inicial * 0.20);
		salario_aumentado = aumento + salario_inicial;
		
		printf("\nSeu aumento de 20 porcento corresponde a: R$:%2.f ", aumento , "reais");
		printf("\nSeu salario com aumento e de: R$:%2.f", salario_aumentado , "reais");
	}
	
	else if (salario_inicial == 280.01 || salario_inicial <= 700.00) {
		printf("\nTem direito a um aumento de 15 porcento");
		
		printf("\nSeu salario anterior e de: R$:%2.f", salario_inicial );
		
		aumento =  ( salario_inicial * 0.15);
		salario_aumentado = aumento + salario_inicial;
		
		printf("\nSeu aumento de 15 porcento corresponde a: R$:%2.f ", aumento , "reais");
		printf("\nSeu salario com aumento e de: R$:%2.f", salario_aumentado , "reais");
		
	}
	else if (salario_inicial == 700.01 || salario_inicial <= 1500.00) {
		printf("\nTem direito a um aumento de 10 porcento");
		
		printf("\nSeu salario anterior e de: R$:%2.f", salario_inicial );
		
		aumento =  ( salario_inicial * 0.10);
		salario_aumentado = aumento + salario_inicial;
		
		printf("\nSeu aumento de 10 porcento corresponde a: R$:%2.f ", aumento , "reais");
		printf("\nSeu salario com aumento e de: R$:%2.f", salario_aumentado , "reais");
		
	}
	
	else if (salario_inicial >= 1500){
		printf("\nTem direito a um aumento de 5 porcento");
		
		printf("\nSeu salario anterior e de: R$:%2.f", salario_inicial );
		
		aumento =  ( salario_inicial * 0.5);
		salario_aumentado = aumento + salario_inicial;
		
		printf("\nSeu aumento de 5 porcento corresponde a: R$:%2.f ", aumento , "reais");
		printf("\nSeu salario com aumento e de: R$:%2.f", salario_aumentado , "reais");
		
	}
	

}
