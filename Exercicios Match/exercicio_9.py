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
