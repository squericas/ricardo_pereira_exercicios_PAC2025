import json
import re

with open('dados.json', 'r', encoding='utf-8') as ficheiro:
    dados = json.load(ficheiro)

padrao_dominio = r'(?:https?://)?(?:www\.)?([\w\.-]+\.\w+)'

for item in dados:
    site = item['site']
    dominio = re.sub(r'https?://', '', site)
    dominio = re.sub(r'www\.', '', dominio)
    print(dominio)
