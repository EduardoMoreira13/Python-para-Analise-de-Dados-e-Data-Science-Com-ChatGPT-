from random import choice

chances = 6
letras_erradas = []
frutas = ["laranja", "uva", "pera", "melancia","abacaxi", "morango", "melão", "jabuticaba", "banana"]
frutas = choice(frutas)
letras_descob = ["-" for i in frutas]


while chances > 0:
    print(f"Número de Chances: {chances}")
    print(f"Letras Erradas: {" ".join(letras_erradas)}")
    print()
    palpite = str(input("Digite uma letra: ")).lower().strip()
    if palpite in frutas:
        indice = 0
        for letra in frutas:
            if letra == palpite:
                letras_descob[indice] = palpite
            indice += 1
    else:
        chances -= 1
        letras_erradas.append(palpite)
    print(f"{" ".join(letras_descob)}")
    if "-" not in " ".join(letras_descob):
        print(f"Parabéns, Você acertou a palavra {frutas}!")
        break
    print()

if chances == 0:
    print(f"Game Over! A palavra correta era {frutas}!")



