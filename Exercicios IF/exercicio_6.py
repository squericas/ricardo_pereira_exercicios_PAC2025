nome = input("Digite o seu nome: ")
valor_compra = 500

if valor_compra > 500:
    desconto = 0.8
    valor_com_desconto = valor_compra * desconto
    percentual = 20
elif 200.01 <= valor_compra <= 500.00:
    desconto = 0.85
    valor_com_desconto = valor_compra * desconto
    percentual = 15
else:
    desconto = 0.9
    valor_com_desconto = valor_compra * desconto
    percentual = 10

valor_do_desconto = valor_compra - valor_com_desconto

print(f"Nome: {nome}")
print(f"Compra: {valor_compra}")
print(f"Desconto: {valor_do_desconto} ({percentual}%)")
print(f"Total a pagar: {valor_com_desconto}")