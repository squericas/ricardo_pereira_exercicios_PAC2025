def mostrar_ascii():
    for i in range(32,127):
        print(i, chr(i))
        if ((i - 31) % 20 == 0):
            input("Enter para mostrar mais 20...")

mostrar_ascii()