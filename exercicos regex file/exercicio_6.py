import re

with open("dados.txt", "r") as file:
        texto = file.read()



padrao_email = r'[\w\.\-]+@[\w\.\-]+\.\w+'
padrao_email_pt = r'[\w\.\-]+@[\w\.\-]+\.pt+'


emails = re.findall(padrao_email,texto)
emails_pt = []
for email in emails:
        emails_pt += re.findall(padrao_email_pt,email)
        
        
print(emails_pt)
