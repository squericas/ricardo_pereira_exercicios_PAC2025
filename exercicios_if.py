## EXERCICIO 1 ##

segundos_totais = int(input("Digite o número de segundos: "))

if segundos_totais < 0:
    print("Insira um valor positivo!")
else:
    horas = segundos_totais // 3600
    minutos = (segundos_totais % 3600) // 60
    segundos = segundos_totais % 60

    resultado = ""

    if horas > 0:
        resultado += f"{horas} {'hora' if horas == 1 else 'horas'}, "
    if minutos > 0:
        resultado += f"{minutos} {'minuto' if minutos == 1 else 'minutos'} e "
    
    resultado += f"{segundos} {'segundo' if segundos == 1 else 'segundos'}."
    
print(resultado)


## EXERCICIO 2 ## 

num1 = 52
num2 = 23
num3 = 11

if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >=num3:
    maior = num2
else:
    maior = num3 

if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

print(f"O maior número é o {maior} e o menor número é o {menor}")


## EXERCICIO 3 ##

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"Ordem crescente: {num1},{num2}")
    print(f"Ordem Decrescente: {num2},{num1}")
else:
    print(f"Ordem crescente: {num2},{num1}")
    print(f"Ordem Decrescente: {num1},{num2}")


## EXERCICIO 4 ##

saldo_cliente = 350
valor_cheque = 300

if valor_cheque > saldo_cliente:
    print("Operação Não concluída. Saldo insuficiente!")
else:
    saldo_cliente -= valor_cheque
    print(f"Cheque de {valor_cheque} euros descontado! Saldo atual: {saldo_cliente} ")


## EXERCICIO 5 ## 

num1 = 52
num2 = 23
num3 = 11

if num1 <= num2 and num1 <= num3:
    menor = num1
    if num2 <= num3:
        meio = num2
        maior = num3
    else:
        meio = num3
        maior = num2
elif num2 <= num1 and num2 <= num3:
    menor = num2
    if num1 <= num3:
        meio = num1 
        maior = num3
    else:
        meio = num3
        maior = num1
else:
    menor = num3
    if num1 <= num2:
        meio = num1
        maior = num2
    else:
        meio = num2
        maior = num1

print(f"Ordem crescente: {menor}, {meio}, {maior}")
print(f"Ordem decrescente: {maior}, {meio}, {menor}")


## EXERCICIO 6 ##

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


## EXERCICIO 8 ##

notas = []
soma = 0
acima_da_media = 0

for aluno in range(1,11):
    while True:
        nota = float(input(f"Digite a nota do aluno {aluno} (0-20): "))
        if 0 <= nota <= 20:
            notas.append(nota)
            soma += nota
            break
        else:
            print("Digite um número de 0-20!")

media = soma / len(notas)

for nota in notas:
    if nota >= media:
        acima_da_media += 1

print(f"Média da turma: {media:.1f}")
print(f"Alunos com nota igual ou acima da média: {acima_da_media}")


## EXERCICIO 9 ##

try:
    mes_numero = int(input("Digite um número de 1 a 12 para saber o mês: "))
    if mes_numero == 1:
        mes_nome = "Janeiro"
    elif mes_numero == 2:
        mes_nome = "Fevereiro"
    elif mes_numero == 3:
        mes_nome = "Março"
    elif mes_numero == 4:
        mes_nome = "Abril"
    elif mes_numero == 5:
        mes_nome = "Maio"
    elif mes_numero == 6:
        mes_nome = "Junho"
    elif mes_numero == 7:
        mes_nome = "Julho"
    elif mes_numero == 8:
        mes_nome = "Agosto"
    elif mes_numero == 9:
        mes_nome = "Setembro"
    elif mes_numero == 10:
        mes_nome = "Outubro"
    elif mes_numero == 11:
        mes_nome = "Novembro"
    elif mes_numero == 12:
        mes_nome = "Dezembro"
    else:
        mes_nome = "Erro: Número inválido! Digite apenas valores entre 1 e 12."

    print(f"Resultado: {mes_nome}")

except ValueError:
    print("Erro: Por favor, digite um número inteiro.")


## EXERCICIO 10 ##

pares = 0
impares = 0
total_numeros = 10

for numero in range (1,total_numeros + 1):
    faltam = total_numeros - numero + 1
    numero_escolhido = int(input(f"Digite um número (faltam {faltam}): "))
    if numero_escolhido % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")