num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"Ordem crescente: {num1},{num2}")
    print(f"Ordem Decrescente: {num2},{num1}")
else:
    print(f"Ordem crescente: {num2},{num1}")
    print(f"Ordem Decrescente: {num1},{num2}")