lista = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]

def contar_minusculas(palavra):
    contador = 0
    for letra in palavra:
        if "a" <= letra <= "z":
            contador += 1
    return contador

def ordenar_minusculas():
    flagtroca = True
    while flagtroca:
        flagtroca = False
        for i in range(len(lista) - 1):
            if contar_minusculas(lista[i]) > contar_minusculas(lista[i+1]):
                lista[i], lista[i+1] = lista[i+1], lista[i]
                flagtroca = True
    return lista

print(ordenar_minusculas())