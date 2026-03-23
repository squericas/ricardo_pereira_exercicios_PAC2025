def numeros_multiplos():
    for i in range(1,1001):
        if i % 5 == 0 and i % 3 != 0:
            print(f"{i} é multiplo de 5 e não é multiplo de 3.")

numeros_multiplos()