""" -- EXERCICIO 1 -- 

dia_da_semana = input("Escreva um dia da semana:").lower()

match dia_da_semana:
    case "segunda-feira" | "terça-feira" | "quarta-feira" | "quinta-feira" | "sexta-feira":
        print("Hoje é dia da semana!")
    case "sábado" | "domingo" :
        print("Hoje é fim de semana!")
    case _:
        print("Esse dia de semana não existe!") """

""" -- EXERCICIO 2 --

nota_teste = float(input("Escreve a nota do teu teste (0-100): "))

match nota_teste:
    case n if 90 <= n <= 100:
        print("Tiveste Excelente!")
    case n if 70 <= n < 90:
        print("Tiveste uma Boa nota!")
    case n if 50 <= n < 70:
        print("Tiveste uma nota Suficiente.")
    case n if n < 50:
        print("Tiveste NEGATIVA!")
    case _:
        print("Nota inválida.") """

""" -- EXERCICIO 3 -- 

tipo_transacao= input("Digite o tipo de transação (Compra/Venda): ").lower()
valor_transacao = float(input("Digite o valor da Transação (€): "))

dicionario = {
    "tipo" : tipo_transacao,
    "valor" : valor_transacao
}

match dicionario:
    case {"tipo" : "venda"}:
        print("Venda de", dicionario["valor"],"euros")
    case {"tipo" : "compra"}:
        print("Compra de", dicionario["valor"],"euros")
    case _:
        print("Pedido desconhecido") """