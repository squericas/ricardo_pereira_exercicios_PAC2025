def tabuada_multiplicacao(numero):
    print("--------")
    print(f"TABUADA DO {numero}")
    print("--------")
    for i in range (1,11):
        multiplicacao = i * numero
        print(f"{numero} x {i} = {multiplicacao}")
        

tabuada_multiplicacao(3)