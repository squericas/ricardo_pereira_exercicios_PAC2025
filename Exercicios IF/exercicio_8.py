notas = []
soma = 0
acima_da_media = 0

for aluno in range(1,11):
    while True:
        nota = float(input(f"Digite a nota do aluno {aluno} (0-20): "))
        if 0 <= nota <= 20:
            notas.append(nota)
            soma += nota
            break
        else:
            print("Digite um número de 0-20!")

media = soma / len(notas)

for nota in notas:
    if nota >= media:
        acima_da_media += 1

print(f"Média da turma: {media:.1f}")
print(f"Alunos com nota igual ou acima da média: {acima_da_media}")
