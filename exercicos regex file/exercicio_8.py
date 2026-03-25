import re

with open("registos.txt", "r") as file:
        texto = file.read()


padrao_data = r'\b\d{2}/\d{2}/\d{4}\b'

datas = re.findall(padrao_data,texto)
print(datas)