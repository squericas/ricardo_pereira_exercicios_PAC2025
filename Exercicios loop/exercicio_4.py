def numero_primo():
    divisores = []
    numero = int(input("Digite um número inteiro para saber se ele é primo: "))
    if numero <= 1:
        return False
    for i in range(1,numero+1):
        if numero % i == 0:
            divisores.append(i)
    if len(divisores) == 2:
        return True
    else:
        return False
    