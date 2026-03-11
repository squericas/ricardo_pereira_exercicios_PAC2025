alunos = []

while True:
    print("1 - Inserir")
    print("2 - Listar")
    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        curso = input("Curso: ")

        aluno = {"nome": nome, "idade": idade, "curso": curso}
        alunos.append(aluno)

    elif opcao == "2":
        for aluno in alunos:
            print("Nome:", aluno["nome"])
            print("Idade:", aluno["idade"])
            print("Curso:", aluno["curso"])
    else:
            print("Opção inválida")