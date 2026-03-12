#introduzir frase
#separar frase
#contar palavras
#guardar

frase = input("Escreva uma frase: ")
palavras = frase.split()
dicionario = {}
for palavra in palavras:
    if palavra in dicionario:
        dicionario[palavra] += 1
    else:
        dicionario[palavra] = 1

print(dicionario)