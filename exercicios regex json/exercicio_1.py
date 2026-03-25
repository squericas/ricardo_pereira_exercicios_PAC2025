import json


with open('dados.json', 'r', encoding='utf-8') as ficheiro:
    dados = json.load(ficheiro)

print(dados)