dia_da_semana = input("Escreva um dia da semana:").lower()

match dia_da_semana:
    case "segunda-feira" | "terça-feira" | "quarta-feira" | "quinta-feira" | "sexta-feira":
        print("Hoje é dia da semana!")
    case "sábado" | "domingo":
        print("Hoje é fim de semana!")
    case _:
        print("Esse dia de semana não existe!")