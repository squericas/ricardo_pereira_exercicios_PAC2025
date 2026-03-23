def numero_primo(numero):
    divisores = []
    
    if numero <= 1:
        return False
    for i in range(1,numero+1):
        if numero % i == 0:
            divisores.append(i)
    return len(divisores) == 2
    
contador = 0
numero = 2
while contador < 10:
    if numero_primo(numero):
        print(f"{contador+1}º número primo: {numero}")
        contador += 1
    numero +=1