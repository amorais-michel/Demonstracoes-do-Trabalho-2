numero_dia= ['1', '2', '3', '4', '5', '6', '7']

numero = input(("Digite um número"))

if numero in numero_dia[0]:
    print("Domingo")

elif numero in numero_dia[1]:
    print("Segunda")

elif numero in numero_dia[2]:
    print("Terça")

elif numero in numero_dia[3]:
    print ("Quarta")

elif numero in numero_dia[4]:
    print("Quinta")

elif numero in numero_dia[5]:
    print("Sexta")

elif numero in numero_dia[6]:
    print("Sabado")

else:
    print("O numero digitado não corresponde a um dia da semana")