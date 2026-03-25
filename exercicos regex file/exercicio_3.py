import re
with open("dados.txt", "r") as file:
        texto = file.read()

padrao_telefone = r'\d{3}(?:[\s\-]?\d{3}){2}'

telefones = re.findall(padrao_telefone,texto)

for telefone in telefones:
        print(telefone)