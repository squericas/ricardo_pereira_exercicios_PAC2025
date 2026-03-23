def tabuada_multiplicacao():
    numero = int(input("Qual é o número que queres aceder à tabuada?: "))
    print("--------")
    print(f"TABUADA DO {numero}")
    print("--------")
    for i in range (1,101):
        multiplicacao = i * numero
        print(f"{numero} x {i} = {multiplicacao}")
        

tabuada_multiplicacao()