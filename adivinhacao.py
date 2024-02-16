import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000
    # rodada = 1
    print("Número secreto:", numero_secreto)

    print("Escolha nível de dificuldade")
    print("(1)Fácil (2)Médio (3)Difícil")
    nivel = int(input("Informe o nível: "))

    if(nivel  == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
    #    print("Tentativa ", rodada, " de ", tentativas)
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("NÚMERO INVÁLIDO: informe número entre 1 e 100")
            continue

        maior = chute > numero_secreto
        menor = chute < numero_secreto
        acertou = chute == numero_secreto

        if(acertou):
            print("Acertou! Vocêz fez {}".format(pontos))
            break
        else:
            if(maior):
                print("Chute menor que número secreto")
            elif(menor):
                print("Chute maior que número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        print("============================================")
      #  rodada = rodada + 1

    print("Fim de jogo")

if(__name__ == "__main__"): #verificação da variável para reproduzir no console
    jogar()