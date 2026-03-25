import re


with open("dados.txt", "r") as file:
        texto = file.read()


padrao_nome = r'(?<=Nome:\s)[^,]+'
padrao_email = r'[\w\.\-]+@[\w\.\-]+\.\w+'
padrao_telefone = r'\d{3}(?:[\s\-]?\d{3}){2}'

nomes = re.findall(padrao_nome,texto)
emails = re.findall(padrao_email,texto)
telefones = re.findall(padrao_telefone,texto)


with open("extraidos.txt", "w") as ficheiro:
        for nome, email, telefone in zip(nomes, emails, telefones):
                ficheiro.write(f" {nome} | {email} | {telefone}\n")
        

