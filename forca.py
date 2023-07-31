import random

banco_de_palavras = ['python', 'javascript', 'java', 'html', 'css', 'php', 'csharp', 'ruby']

def sorteio():
    return random.choice(banco_de_palavras)

def verificar(palavra, letra, letras_corretas):
    if letra in palavra:
        letras_corretas.add(letra)
        return True
    return False

def mostrar(palavra, letras_corretas):
    palavra_secreta = ""
    for letra in palavra:
        if letra in letras_corretas:
            palavra_secreta += letra
        else:
            palavra_secreta += "_"
    return palavra_secreta

def game():
    palavra = sorteio()
    letras_corretas = set()
    tentativas = 6

    while True:
        menu=int(input("Bem Vindos a forca de linguagens de programação\n1-jogar\n2-regras\n0-sair"))
        if menu==1:
            while True:
                palavra_secreta = mostrar(palavra, letras_corretas)
                print(f"Palavra: {palavra_secreta}")
                print(f"Tentativas restantes: {tentativas}")

                if palavra == palavra_secreta:
                    print("Parabéns, você venceu!")
                    break

                letra = (input("Digite uma letra: ")).lower()
                if letra in letras_corretas:
                    print("Você já tentou esta letra.")
                elif verificar(palavra, letra, letras_corretas):
                    print("Letra correta!")
                else:
                    print("Letra incorreta.")
                    tentativas -= 1

                if tentativas == 0:
                    print("Game Over. A palavra era:", palavra)
                    break
        if menu ==2:
            print("Selecione a palavra e coloque um traço por cada letra;\nQuem está a adivinhar a palavra diz uma letra de cada vez;\nSe acertar escreve-se a letra no respetivo lugar;\nSe errar, começa a desenhar-se o boneco (primeiro a cabeça, depois o tronco, de seguida pernas e braços);\nO jogador perde se não conseguir identificar a palavra antes do desenho estar completo;")
        if menu ==0:
            print("Valeu ai!")
            break

def main():
    print("Jogo da Forca")
    print("==============")
    game()

if __name__ == "__main__":
    main()

