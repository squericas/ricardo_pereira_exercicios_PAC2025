palavra = "abcedario"
caracteres = list(palavra)

def ordenar_palavra():
    flagtroca = True
    while flagtroca:
        flagtroca=False
        for i in range(len(caracteres)-1):
            if caracteres[i] > caracteres[i+1]:
                caracteres[i],caracteres[i+1] = caracteres[i+1],caracteres[i]
                flagtroca=True
    palavra_ordenada = "".join(caracteres)
    return palavra_ordenada

print(ordenar_palavra())