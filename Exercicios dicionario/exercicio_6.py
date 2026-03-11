vendas = {'Janeiro': 1000, 'Fevereiro': 1500, 'Março': 1200}

media = 0
#contar numero de meses (contar chaves) 
#somar valores
#dividir valores por chaves

media = sum(vendas.values()) / len(vendas.keys())

print(f"A média de vendas é: €{media:.2f}")