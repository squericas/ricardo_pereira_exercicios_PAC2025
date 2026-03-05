def calcular_media():
    contador = 0
    soma = 0
    media = 0
    while contador < 30:
        try:
            numero = int(input("Introduza um número par entre 1 e 50: "))
            if 1 <= numero and 50 >= numero and numero % 2 == 0:
                soma += numero
                contador += 1
            else:
                print("Número inválido.")
        except:
            print("Introduza um número inteiro.") 
    media = soma / contador
    print(f"Média = {media}")   

calcular_media()
