def pedir_numero():
        numero = int(input("Digite um Número de 1 a 100: "))
        while numero < 1 or numero > 100:
                print("Número inválido! digite um número de 1 a 100!")
                numero = int(input("Digite um Número de 1 a 100: "))
        print(f"Número válido. Número escolhido: {numero}")

pedir_numero()