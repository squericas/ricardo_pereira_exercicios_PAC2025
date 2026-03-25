import re
with open("dados.txt", "r") as file:
        texto = file.read()


padrao_nome = r'(?<=Nome:\s)[^,]+'

nomes = re.findall(padrao_nome,texto)

for nome in nomes:
        print(nome)