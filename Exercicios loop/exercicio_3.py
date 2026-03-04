def analisar_notas():
    notas_turma = []
    soma = 0
    for aluno in range(1,11):
        nota_aluno = float(input(f"Digite a nota do aluno {aluno} (0-20):"))
        if 0 <= nota_aluno <= 20:
            notas_turma.append(nota_aluno)
            soma += nota_aluno
        else:
            print("Digite um número de 0-20!")
    media = soma / len(notas_turma)
    return f"A média da turma é {media}"

print(analisar_notas())