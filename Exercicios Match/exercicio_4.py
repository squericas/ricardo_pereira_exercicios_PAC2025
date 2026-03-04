valor = "34543543543"

def analisar(valor):
    match valor:
        case int():
            return "Número inteiro"
        case float():
            return "Número decimal"
        case str() as s:
            try:
                float(s)
                return "String numérica"
            except ValueError:
                return "String textual"
        case list():
            return "Lista"
        case _:
            return "Tipo desconhecido"

print(analisar(valor))