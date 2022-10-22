print("--------------------------------------")
print("|  Bem vindo ao jogo de adivinhacao  |")
print("--------------------------------------")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1
while(rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada,total_de_tentativas)) #Interpolation
    chute = int(input("Digite seu numero: "))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Voce acertou+++++++++++")
    else:
        if(maior):
            print("Voce errou seu chute foi maior que o chute secreto")
        elif(menor):
            print("Voce errou seu chute foi menor que o numero secreto")
    rodada+=1


print("Fim de jogo")

