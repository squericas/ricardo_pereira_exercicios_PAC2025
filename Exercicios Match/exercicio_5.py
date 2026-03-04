def analisar(mensagem):
    msg = mensagem.lower().strip()
    match msg:
        case "olá" | "bom dia":
            return "Saudação"
        case _:
            if "tchau" in msg or "adeus" in msg:
                return "Despedida"
            elif msg.endswith("?"):
                return "Pergunta"
            else:
                return "Mensagem Genérica"

print(analisar("olá"))
print(analisar("bom dia"))
print(analisar("Vou bazar, tchau"))
print(analisar("Tudo bem?"))
print(analisar("Nada a ver"))