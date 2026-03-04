pares = 0
impares = 0
total_numeros = 10

for numero in range (1,total_numeros + 1):
    faltam = total_numeros - numero + 1
    numero_escolhido = int(input(f"Digite um número (faltam {faltam}): "))
    if numero_escolhido % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")