import random

def play():

    message()

    palavra_secreta = secret_word()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip().lower()
        print(f"Rodada {tentativas}")
    
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = chute
                    print(f"Acertou a letra: {chute} na posição {index}")
                index = index + 1
        else:
            print("Você errou :(")
            tentativas = tentativas + 1
        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    
    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

def message():
    print("*********************************")
    print("***Seja bem vindo ao jogo da forca!***")
    print("*********************************")

def secret_word():
    palavras = []
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].strip().lower()
    
    return palavra_secreta

if(__name__ == "__main__"):
    play()