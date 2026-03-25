import re

with open("registos.txt", "r") as file:
        texto = file.read()
padrao_dominio = r'(?<=Site:\s)(?:https?://)?(?:www\.)?([\w\.-]+\.\w+)'
sites = re.findall(padrao_dominio,texto)
print(sites)