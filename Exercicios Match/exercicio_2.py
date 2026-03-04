nota_teste = float(input("Escreve a nota do teu teste (0-100): "))

match nota_teste:
    case n if 90 <= n <= 100:
        print("Tiveste Excelente!")
    case n if 70 <= n < 90:
        print("Tiveste uma Boa nota!")
    case n if 50 <= n < 70:
        print("Tiveste uma nota Suficiente.")
    case n if n < 50:
        print("Tiveste NEGATIVA!")
    case _:
        print("Nota inválida.")