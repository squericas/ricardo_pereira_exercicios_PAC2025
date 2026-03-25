import re
with open("dados.txt", "r") as file:
        texto = file.read()

padrao_email = r'[\w\.\-]+@[\w\.\-]+\.\w+'

emails = re.findall(padrao_email,texto)

for email in emails:
        print(email)