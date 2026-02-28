# ==================================================
# EXERCICIO 1
# ==================================================

dia_da_semana = input("Escreva um dia da semana:").lower()

match dia_da_semana:
    case "segunda-feira" | "terça-feira" | "quarta-feira" | "quinta-feira" | "sexta-feira":
        print("Hoje é dia da semana!")
    case "sábado" | "domingo":
        print("Hoje é fim de semana!")
    case _:
        print("Esse dia de semana não existe!")


# ==================================================
# EXERCICIO 2
# ==================================================

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
        print("Nota inválida.")


# ==================================================
# EXERCICIO 3
# ==================================================

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


# ==================================================
# EXERCICIO 4
# ==================================================

valor = "34543543543"

def analisar(valor):
    match valor:
        case int():
            return "Número inteiro"
        case float():
            return "Número decimal"
        case str() as s:
            try:
                float(s)
                return "String numérica"
            except ValueError:
                return "String textual"
        case list():
            return "Lista"
        case _:
            return "Tipo desconhecido"

print(analisar(valor))


# ==================================================
# EXERCICIO 5
# ==================================================

def analisar(mensagem):
    msg = mensagem.lower().strip()
    match msg:
        case "olá" | "bom dia":
            return "Saudação"
        case _:
            if "tchau" in msg or "adeus" in msg:
                return "Despedida"
            elif msg.endswith("?"):
                return "Pergunta"
            else:
                return "Mensagem Genérica"

print(analisar("olá"))
print(analisar("bom dia"))
print(analisar("Vou bazar, tchau"))
print(analisar("Tudo bem?"))
print(analisar("Nada a ver"))


# ==================================================
# EXERCICIO 6
# ==================================================

def analisar_servidor(dicionario):
    ping_alto = 200
    match dicionario:
        case {"status": "ok", "tempo_resposta": tempo} if tempo > ping_alto:
            return "Servidor lento"
        case {"status": "ok"}:
            return "Servidor ativo"
        case {"status": "erro"}:
            return "Servidor indisponível"
        case _:
            return "Estado desconhecido"

print(analisar_servidor({"status": "ok", "tempo_resposta": 290}))
print(analisar_servidor({"status": "ok", "tempo_resposta": 200}))
print(analisar_servidor({"status": "erro", "tempo_resposta": 290}))


# ==================================================
# EXERCICIO 7
# ==================================================

def analisar_produto(dicionario):
    produto_luxo = 1000
    match dicionario:
        case {"categoria": "eletronico", "preco": preco} if preco > produto_luxo:
            return "Produto de luxo"
        case {"categoria": "eletronico", "preco": preco} if preco <= produto_luxo:
            return "Produto comum"
        case {"categoria": "alimento"}:
            return "Produto alimentar"
        case _:
            return "Categoria desconhecida"

print(analisar_produto({"categoria": "eletronico", "preco": 1000}))
print(analisar_produto({"categoria": "eletronico", "preco": 2000}))
print(analisar_produto({"categoria": "alimento", "preco": 1000}))
print(analisar_produto({"categoria": "padaria", "preco": 1000}))


# ==================================================
# EXERCICIO 8
# ==================================================

def somar_numeros(n1, n2):
    return n1 + n2

def subtrair_numeros(n1, n2):
    return n1 - n2

def multiplicar_numeros(n1, n2):
    return n1 * n2

def dividir_numeros(n1, n2):
    return n1 / n2

operacao = input("Qual é a operação? (Somar/Subtrair/Multiplicar/Dividir)").lower()

match operacao:
    case "somar":
        n1 = float(input("Qual o primeiro número?: "))
        n2 = float(input("Qual o segundo número?: "))
        print(somar_numeros(n1, n2))
    case "subtrair":
        n1 = float(input("Qual o primeiro número?: "))
        n2 = float(input("Qual o segundo número?: "))
        print(subtrair_numeros(n1, n2))
    case "multiplicar":
        n1 = float(input("Qual o primeiro número?: "))
        n2 = float(input("Qual o segundo número?: "))
        print(multiplicar_numeros(n1, n2))
    case "dividir":
        n1 = float(input("Qual o primeiro número?: "))
        n2 = float(input("Qual o segundo número?: "))
        print(dividir_numeros(n1, n2))
    case _:
        print("Operação inválida")


# ==================================================
# EXERCICIO 9
# ==================================================

def analisar_request(dicionario):
    match dicionario:
        case {"metodo": "GET"}:
            return "Requisição GET recebida"
        case {"metodo": "POST", "conteudo": conteudo} if len(conteudo) > 0:
            return "Requisição POST com dados válidos"
        case {"metodo": "POST", "conteudo": conteudo} if conteudo == "":
            return "Requisição POST sem dados"
        case _:
            return "Método não suportado"

print(analisar_request({"metodo": "GET", "conteudo": ""}))
print(analisar_request({"metodo": "POST", "conteudo": "123"}))
print(analisar_request({"metodo": "POST", "conteudo": ""}))
print(analisar_request({"metodo": "led", "conteudo": ""}))


# ==================================================
# EXERCICIO 10
# ==================================================

jogador1 = input("Jogador 1 (Pedra/Papel/Tesoura): ").lower()
jogador2 = input("Jogador 2 (Pedra/Papel/Tesoura): ").lower()

match (jogador1, jogador2):
    case _ if jogador1 == jogador2:
        print("Empate")
    case ("pedra", "tesoura"):
        print("Jogador 1 Venceu")
    case ("tesoura", "papel"):
        print("Jogador 1 venceu")
    case ("papel", "pedra"):
        print("Jogador 1 venceu")
    case ("tesoura", "pedra"):
        print("Jogador 2 venceu")
    case ("papel", "tesoura"):
        print("Jogador 2 venceu")
    case ("pedra", "papel"):
        print("Jogador 2 venceu")
    case _:
        print("Jogada inválida")