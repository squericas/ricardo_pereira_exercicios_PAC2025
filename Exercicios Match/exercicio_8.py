def somar_numeros(n1, n2):
    return n1 + n2

def subtrair_numeros(n1, n2):
    return n1 - n2

def multiplicar_numeros(n1, n2):
    return n1 * n2

def dividir_numeros(n1, n2):
    return n1 / n2

operacao = input("Qual é a operação? (Somar/Subtrair/Multiplicar/Dividir)").lower()

match operacao:
    case "somar":
        n1 = float(input("Qual o primeiro número?: "))
        n2 = float(input("Qual o segundo número?: "))
        print(somar_numeros(n1, n2))
    case "subtrair":
        n1 = float(input("Qual o primeiro número?: "))
        n2 = float(input("Qual o segundo número?: "))
        print(subtrair_numeros(n1, n2))
    case "multiplicar":
        n1 = float(input("Qual o primeiro número?: "))
        n2 = float(input("Qual o segundo número?: "))
        print(multiplicar_numeros(n1, n2))
    case "dividir":
        n1 = float(input("Qual o primeiro número?: "))
        n2 = float(input("Qual o segundo número?: "))
        print(dividir_numeros(n1, n2))
    case _:
        print("Operação inválida")