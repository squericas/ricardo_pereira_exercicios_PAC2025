def analisar_servidor(dicionario):
    ping_alto = 200
    match dicionario:
        case {"status": "ok", "tempo_resposta": tempo} if tempo > ping_alto:
            return "Servidor lento"
        case {"status": "ok"}:
            return "Servidor ativo"
        case {"status": "erro"}:
            return "Servidor indisponível"
        case _:
            return "Estado desconhecido"

print(analisar_servidor({"status": "ok", "tempo_resposta": 290}))
print(analisar_servidor({"status": "ok", "tempo_resposta": 200}))
print(analisar_servidor({"status": "erro", "tempo_resposta": 290}))
