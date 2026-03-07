

def mostrar_fibonacci():
    numero1 = 1
    numero2 = 1
    lista_fibonacci = [numero1,numero2]
    soma = 0
    while len(lista_fibonacci) < 60:
            soma = numero1 + numero2
            lista_fibonacci.append(soma)
            numero1 = numero2
            numero2 = soma
    return lista_fibonacci
    

print(mostrar_fibonacci())