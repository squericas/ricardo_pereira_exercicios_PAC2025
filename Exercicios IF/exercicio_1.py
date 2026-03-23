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
