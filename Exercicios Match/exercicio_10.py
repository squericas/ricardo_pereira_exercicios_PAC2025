jogador1 = input("Jogador 1 (Pedra/Papel/Tesoura): ").lower()
jogador2 = input("Jogador 2 (Pedra/Papel/Tesoura): ").lower()

match (jogador1, jogador2):
    case _ if jogador1 == jogador2:
        print("Empate")
    case ("pedra", "tesoura"):
        print("Jogador 1 Venceu")
    case ("tesoura", "papel"):
        print("Jogador 1 venceu")
    case ("papel", "pedra"):
        print("Jogador 1 venceu")
    case ("tesoura", "pedra"):
        print("Jogador 2 venceu")
    case ("papel", "tesoura"):
        print("Jogador 2 venceu")
    case ("pedra", "papel"):
        print("Jogador 2 venceu")
    case _:
        print("Jogada inválida")