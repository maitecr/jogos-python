import adivinhacao
import forca

def escolha_jogo():
    print("*********************************")
    print("******Escolha o seu jogo!********")
    print("*********************************")

    print("(1)Adivinhação (2)Forca")
    jogo = int(input("Escolha o jogo: "))

    if(jogo == 1 ):
        print("Adivinhação")
        adivinhacao.jogar()
    elif(jogo == 2):
        print("Forca")
        forca.jogar()

if(__name__ == "__main__"):
    escolha_jogo()

