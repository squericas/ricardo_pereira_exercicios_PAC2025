try:
    mes_numero = int(input("Digite um número de 1 a 12 para saber o mês: "))
    if mes_numero == 1:
        mes_nome = "Janeiro"
    elif mes_numero == 2:
        mes_nome = "Fevereiro"
    elif mes_numero == 3:
        mes_nome = "Março"
    elif mes_numero == 4:
        mes_nome = "Abril"
    elif mes_numero == 5:
        mes_nome = "Maio"
    elif mes_numero == 6:
        mes_nome = "Junho"
    elif mes_numero == 7:
        mes_nome = "Julho"
    elif mes_numero == 8:
        mes_nome = "Agosto"
    elif mes_numero == 9:
        mes_nome = "Setembro"
    elif mes_numero == 10:
        mes_nome = "Outubro"
    elif mes_numero == 11:
        mes_nome = "Novembro"
    elif mes_numero == 12:
        mes_nome = "Dezembro"
    else:
        mes_nome = "Erro: Número inválido! Digite apenas valores entre 1 e 12."

    print(f"Resultado: {mes_nome}")

except ValueError:
    print("Erro: Por favor, digite um número inteiro.")