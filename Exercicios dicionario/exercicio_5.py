palavra = input("Digite uma palavra: ")
letras = {}
for letra in palavra:
    if letra in letras:
        letras[letra] += 1
    else:
        letras[letra] = 1

print(letras)