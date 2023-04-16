print("*********************************")
print("*Bem vindo ao jogo de Advinhação*")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite um número entre 1 e 100: \n"))
    print("Você digitou:", chute)
    acertou = chute == numero_secreto
    menor = chute < numero_secreto
    maior = chute > numero_secreto

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue #Sai desta interação

    if(acertou):
        print("Você acertou!")
        break #Sai do laço
    else:
        if(maior):
            print("Seu chute foi MAIOR do que o número secreto!")
        elif(menor):
            print("Seu chute foi MENOR do que o número secreto!")
    
print("Fim de jogo")