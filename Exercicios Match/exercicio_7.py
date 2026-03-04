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