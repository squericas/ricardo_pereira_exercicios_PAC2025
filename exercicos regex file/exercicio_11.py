import re

with open("registos.txt", "r") as file:
        texto = file.read()


padrao_nif_valido = r'[1|2|3|5|6|8]\d{8}'

nifs_validos = re.findall(padrao_nif_valido,texto)
for nif in nifs_validos:
        print(nif)