lista = ["Rede", "Python", "inteligência", "dados", "Aprender"]

def ordenar_lista():
    flagtroca = True
    while flagtroca:
        flagtroca = False
        for i in range(len(lista)-1):
                if ord(lista[i][0].lower()) < ord(lista[i+1][0].lower()):
                    lista[i],lista[i+1] = lista[i+1],lista[i]
                    flagtroca = True
    return lista

print(ordenar_lista())