frequencia = int(input("Digite a frequencia:"))

nota1 = int(input("Digite sua nota:"))
nota2 = int(input("Digite outra nota:"))

media = 0
notanecessaria = 0


# verificando se o valor das notas 1 e 2 sao validos.

if nota1 and nota2 == 0 or nota1 and nota2 <= 10:  # verificando se a nota digitada tá entre 0 e 10
    if frequencia == 0 or frequencia <= 100:  # verificando se o valor da frequencia é valido

        media = (nota1 + nota2) / 2
        pontos_faltam_g1 = ((nota1+nota2) + nota1)
        pontos_faltam_g2 = (nota1 + nota2) + nota2

        media_nova1 = (pontos_faltam_g1 + nota2) /2
        media_nova2 = (pontos_faltam_g2 + nota1) /2

        if frequencia < 75:
            print("\nReprovado por falta de frequencia")
        elif media >= 6:
            print("\nAprovado com média: ", media)

        elif nota1 and nota2 or nota2 and nota1 < 2:
            print("\nReprovado por insuficiencia de nota!")
            if nota1 < nota2:
                print("\nPrecisa substituir G1 e tirar:", pontos_faltam_g1, " pontos, assim teras uma media de:", media_nova1  )
            elif nota2 < nota1:
                print("\nPrecisa substituir G2 e tirar:", pontos_faltam_g2, "pontos, assim teras uma media de:", media_nova2)
            elif nota1 == nota2:
                print("\nO aluno pode escolher o grau a substituir e tirar:", nota1+nota2 )

    else:
        print("\nDigite um valor de frequencia decente")

else:
    print("\nDigite um valor de nota decente")
