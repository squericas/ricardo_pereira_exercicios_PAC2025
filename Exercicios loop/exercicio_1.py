def analisar_numero(numero):
    if numero % 2 == 0:
        return f"Número: {numero}: Par"
    else:
        return f"Número: {numero}: Impar"

for numero in range (1,31):
    print(analisar_numero(numero))