import re

with open("registos.txt", "r") as file:
        texto = file.read()


padrao_postalcode = r'\d{4}\-\d{3}'

postalcode = re.findall(padrao_postalcode,texto)
print(postalcode)