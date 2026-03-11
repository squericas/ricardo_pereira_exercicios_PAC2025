dicionario = {'a': 1, 'b': 2, 'c': 3}
novo_dicionario = {}

#criar novo dicionario 
#percorrer todas as chaves do dicionário original e adicionar como valor ao novo dicionario
for chave in dicionario:
    valor = dicionario[chave]
    novo_dicionario[valor] = chave

print(novo_dicionario)