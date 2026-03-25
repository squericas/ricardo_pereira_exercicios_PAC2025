import re
with open("registos.txt", "r") as file:
        texto = file.read()


padrao_nome = r'(?<=Nome:\s)[^|]+'
padrao_telefone = r'\d{3}(?:[\s\-]?\d{3}){2}'
padrao_data = r'\b\d{2}/\d{2}/\d{4}\b'
padrao_nif = r'\b\d{9}\b'
padrao_dominio = r'(?<=Site:\s)(?:https?://)?(?:www\.)?([\w\.-]+\.\w+)'

nomes = re.findall(padrao_nome,texto)
sites = re.findall(padrao_dominio,texto)
telefones = re.findall(padrao_telefone,texto)
datas = re.findall(padrao_data,texto)
nifs = re.findall(padrao_nif,texto)


with open("resumo.txt", "w") as ficheiro:
        for nome, nif,data,telefone,site  in zip(nomes, nifs, datas,telefones,sites):
                ficheiro.write(f" {nome} | {nif} | {telefone} | {data} | {site}\n")