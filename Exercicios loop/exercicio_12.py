def operacoes_com_numeros(numero):
    count_operacoes = 0
    for i in range(1,numero):
        soma = numero + i
        subtracao = numero - i
        multiplicacao = numero * i
        divisao = numero / i
        print(f"{numero} + {i} = {soma}")
        print(f"{numero} - {i} = {subtracao}")
        print(f"{numero} / {i} = {divisao}")
        print(f"{numero} * {i} = {multiplicacao}")
        print("------------")
        count_operacoes += 4

    print(f"Total de operações realizadas: {count_operacoes}")


operacoes_com_numeros(60)