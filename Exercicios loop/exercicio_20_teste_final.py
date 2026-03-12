def numero_primo(numero):
    if numero <= 1:
        return False
    
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)

    return len(divisores) == 2


def numero_perfeito(numero):
    soma = 0
    for valor in range(1, numero):
        if numero % valor == 0:
            soma += valor

    return soma == numero


def calcular_divisores(numero):
    contador = []
    
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador.append(i)

    return contador


def tabuada():
    numero = int(input("Número da tabuada: "))
    limite = int(input("Até que número multiplicar (máx 1000): "))

    if limite < 1 or limite > 1000:
        print("Valor inválido")
        return

    contador = 0

    for i in range(1, limite + 1):
        print(f"{numero} x {i} = {numero * i}")
        contador += 1

        if contador % 20 == 0:
            input("Carrega ENTER para continuar")


def calculadora():
    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))
    op = input("Operação (+,-,*,/): ")

    if op == "+":
        print(n1 + n2)
    elif op == "-":
        print(n1 - n2)
    elif op == "*":
        print(n1 * n2)
    elif op == "/":
        if n2 != 0:
            print(n1 / n2)
        else:
            print("Divisão por zero!")
    else:
        print("Operação inválida")


def analisar_numeros():
    numero = int(input("Introduza um número entre 1 e 30000: "))

    if numero < 1 or numero > 30000:
        print("Número inválido")
        return

    contador = 0

    for i in range(1, numero + 1):

        divisores = calcular_divisores(i)

        print(f"\nNúmero: {i}")
        print(f"Divisores: {divisores}")
        print(f"Quantidade de divisores: {len(divisores)}")

        if numero_primo(i):
            print("É número primo")

        if numero_perfeito(i):
            print("É número perfeito")

        contador += 1

        if contador % 10 == 0:
            input("Carrega ENTER para continuar")


while True:

    print("1 - Analisar números")
    print("2 - Calculadora")
    print("3 - Tabuada")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        analisar_numeros()

    elif opcao == "2":
        calculadora()

    elif opcao == "3":
        tabuada()

    elif opcao == "4":
        print("Programa terminado")
        break

    else:
        print("Opção inválida")