def numero_perfeito(numero):
    soma = 0
    for valor in range (1,numero):
        if numero % valor == 0:
            soma += valor
    return soma == numero
        

def exibir_numero():
    numero = int(input("Exibir numeros perfeitos até ao número: "))
    for valor in range (1,numero+1):
        if(numero_perfeito(valor)):
            print(valor)
            
while True:
    exibir_numero()
