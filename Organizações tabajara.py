
#pedindo nome do usuario
nome = input("\nDigite seu nome:")

#pedindo salario do usuario
salario_antes_reajuste = float(input("Informe seu salário em digitos:"))

#verificando se o salario do usuario é igual a 280 reais
if salario_antes_reajuste <= 280.00:
    print("\nTem direito a um ganho de 20% de aumento, caro" , nome)
    print("Seu salário antes do reajuste é de :", salario_antes_reajuste ,"reais")

    #calculando e exibindo na tela quantos porcento é o aumento do salário do usuario
    aumento_salario_valor = (salario_antes_reajuste * 0.20)
    print("Valor do aumento é de:", aumento_salario_valor,"reais")

    #calculando e imprimindo na tela o valor do salario novo do usuario
    salario_novo = (salario_antes_reajuste + aumento_salario_valor)
    print("O teu salário novo é de:", salario_novo ,"reais")

elif salario_antes_reajuste == 280.01 or salario_antes_reajuste <= 700.00:
    print("\nTem direito a um ganho de 15% de aumento, caro", nome)
    print("Seu salário antes do reajuste é de :", salario_antes_reajuste ,"reais")

    # calculando e exibindo na tela quantos porcento é o aumento do salário do usuario
    aumento_salario_valor = (salario_antes_reajuste * 0.15)
    print("Valor do aumento é de:", aumento_salario_valor ,"reais")

    # calculando e imprimindo na tela o valor do salario novo do usuario
    salario_novo = (salario_antes_reajuste + aumento_salario_valor)
    print("O teu salário novo é de:", salario_novo  ,"reais")

elif salario_antes_reajuste == 700.01 or salario_antes_reajuste <= 1500.00 :
    print("\nTem direito a um ganho de 10% de aumento, caro", nome)
    print("Seu salário antes do reajuste é de :", salario_antes_reajuste ,"reais")

    # calculando e exibindo na tela quantos porcento é o aumento do salário do usuario
    aumento_salario_valor = (salario_antes_reajuste * 0.10)
    print("Valor do aumento é de:", aumento_salario_valor ,"reais")

    # calculando e imprimindo na tela o valor do salario novo do usuario
    salario_novo = (salario_antes_reajuste + aumento_salario_valor)
    print("O teu salário novo é de:", salario_novo ,"reais")

elif salario_antes_reajuste >= 1500.01 :
    print("\nTem direito a um ganho de 5% de aumento, caro", nome)
    print("Seu salário antes do reajuste é de :", salario_antes_reajuste ,"reais")

    # calculando e exibindo na tela quantos porcento é o aumento do salário do usuario
    aumento_salario_valor = (salario_antes_reajuste * 0.5)
    print("Valor do aumento é de:", aumento_salario_valor ,"reais")

    # calculando e imprimindo na tela o valor do salario novo do usuario
    salario_novo = (salario_antes_reajuste + aumento_salario_valor)
    print("O teu salário novo é de: %.2f" %( salario_novo) ,"reais")

else:
    print("Salario imcompativel com a empresa")