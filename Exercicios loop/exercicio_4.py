def numero_primo():
    numero = int(input("Digite um número inteiro para saber se ele é primo: "))
    
    if numero <= 1:
        return False
    
    divisores = []
    
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    
    return len(divisores) == 2


if numero_primo():
    print("É primo")
else:
    print("Não é primo")