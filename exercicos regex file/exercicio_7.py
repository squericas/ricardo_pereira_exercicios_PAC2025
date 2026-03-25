import re

with open("registos.txt", "r") as file:
        texto = file.read()


padrao_nif = r'\b\d{9}\b'

nifs = re.findall(padrao_nif,texto)
for nif in nifs:
        print(nif)