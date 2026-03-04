def analisar_numero_par_impar(numero):
    if numero % 2 == 0:
        return "Número par"
    else:
        return "Número ímpar"

for i in range(1,11):
    numero_escolhido = int(input("Digite um número para saber se é par ou ímpar: "))
    print(analisar_numero_par_impar(numero_escolhido))