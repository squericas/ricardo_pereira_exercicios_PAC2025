tipo_transacao = input("Digite o tipo de transação (Compra/Venda): ").lower()
valor_transacao = float(input("Digite o valor da Transação (€): "))

dicionario = {
    "tipo": tipo_transacao,
    "valor": valor_transacao
}

match dicionario:
    case {"tipo": "venda"}:
        print("Venda de", dicionario["valor"], "euros")
    case {"tipo": "compra"}:
        print("Compra de", dicionario["valor"], "euros")
    case _:
        print("Pedido desconhecido")