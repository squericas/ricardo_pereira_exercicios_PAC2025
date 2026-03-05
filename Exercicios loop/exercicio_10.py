def calcular_divisores(numero):
    contador = []
    for i in range (1,numero + 1):
        if numero % i == 0:
            contador.append(i)
    print(f"quantidade de divisores: {len(contador)}")
    print(f"Divisores: {contador}")

calcular_divisores(10)