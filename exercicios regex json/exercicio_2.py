import json
import re

with open('dados.json', 'r', encoding='utf-8') as ficheiro:
    dados = json.load(ficheiro)

padrao_email = r'[\w\.\-]+@[\w\.\-]+\.\w+'

for item in dados:
    email = item['email']
    if re.match(padrao_email,email):
        print(f'{email} E-mail Válido')
    else:
        print(f'{email} E-mail Inválido')
