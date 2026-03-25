import json
import re

with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)
    

padrao_nif_valido = r'[1|2|3|5|6|8]\d{8}'
padrao_email = r'[\w\.\-]+@[\w\.\-]+\.\w+'
registos_validos = []

for pessoa in dados:
    validar_email = re.match(padrao_email,pessoa['email'])
    validar_nif = re.match(padrao_nif_valido,pessoa['nif'])
    telefone = re.sub(r'\D','',pessoa['telemovel'])
    validar_telefone = len(telefone) == 9

    if validar_email and validar_nif and validar_telefone:
        registos_validos.append(pessoa)
with open('validos.json', 'w', encoding='utf-8') as ficheiro_saida:
    json.dump(registos_validos, ficheiro_saida, indent=4, ensure_ascii=False)

