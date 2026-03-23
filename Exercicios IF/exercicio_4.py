saldo_cliente = 350
valor_cheque = 300

if valor_cheque > saldo_cliente:
    print("Operação Não concluída. Saldo insuficiente!")
else:
    saldo_cliente -= valor_cheque
    print(f"Cheque de {valor_cheque} euros descontado! Saldo atual: {saldo_cliente} ")