import re
from datetime import datetime
with open("registos.txt", "r") as file:
        texto = file.read()


padrao_data = r'\d{2}/\d{2}/\d{4}'


datas_encontradas = re.findall(padrao_data, texto)


for data_string in datas_encontradas:

    data = datetime.strptime(data_string, "%d/%m/%Y")
    
    # Verificar se o ano é menor que 2025
    if data.year < 2025:
        print (f'{data.year} "{data}"')
