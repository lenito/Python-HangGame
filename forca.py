import random

def jogar():

    print("*"* 33)
    print("***Bem vindo ao jogo da Forca!***")
    print("*" * 33)

    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()

    num_lista = random.randrange(0,len(palavras)-1)

    print(palavras[num_lista])

    palavra_secreta = palavras[num_lista].upper()
    letras_acertadas = ["-", "-", "-", "-", "-", "-"]

    print("A palavra é assim ", "__ "*len(palavra_secreta))

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute==letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        acertou = "-" not in letras_acertadas
        enforcou = erros == 6
        print(letras_acertadas)
    print("Fim de Jogo")


if(__name__ == "__main__"):
    jogar()