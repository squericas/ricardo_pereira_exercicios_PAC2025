import json
import re

with open('dados.json', 'r', encoding='utf-8') as ficheiro:
    dados = json.load(ficheiro)

padrao_nif_valido = r'[1|2|3|5|6|8]\d{8}'

for nif in dados:
    nif = nif['nif']
    if re.match(padrao_nif_valido, nif):
        print(f'{nif} NIF Válido')
    else:
        print(f'{nif} NIF Inválido')

