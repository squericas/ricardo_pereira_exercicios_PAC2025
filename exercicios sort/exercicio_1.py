listafrutas = ["banana","barreira", "uva", "abacaxi","abacate","laranja"]

def ordenar_lista():
    flagtroca = True
    while flagtroca:
        flagtroca = False
        for i in range(len(listafrutas)-1):
                for t in range(len(listafrutas[i])):
                    if listafrutas[i][t] > listafrutas[i+1][t]:
                        listafrutas[i],listafrutas[i+1] = listafrutas[i+1],listafrutas[i]
                        flagtroca = True
    return listafrutas

print(ordenar_lista())