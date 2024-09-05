import random
import os

path_file = os.path.join(os.path.dirname(__file__), 'br-sem-acentos.txt')

with open(path_file, "r", encoding="UTF-8") as arquivo:
    lista_de_palavras = [linha.strip() for linha in arquivo]

palavra = random.choice(lista_de_palavras)
letras_usuario = []
chances = 6
ganhou = False

while True:
    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_",end=" ")
    print(f"Você tem {chances}")
    tentativa = input("Digite uma letra: ")
    letras_usuario.append(tentativa)
    if tentativa.lower() not in palavra.lower():
        chances -= 1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Parabéns, Você ganhou! A palavra era: {palavra}")
else:
    print(f"Que pena, Você perdeu! A palavra era {palavra}")

    
