# ==========================================
# CLIENTE TCP EM PYTHON
# Ligação a um servidor usando SOCKET
# ==========================================

import socket     # biblioteca para comunicação em rede
import time       # biblioteca para controlo de tempo (opcional)


# -------------------------------
# 1. CRIAR A SOCKET
# -------------------------------
# AF_INET  -> usa IPv4
# SOCK_STREAM -> usa protocolo TCP

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# -------------------------------
# 2. DEFINIR DADOS DO SERVIDOR
# -------------------------------

host = "127.0.0.1"   # endereço do servidor (localhost)
porta = 12340        # porta do servidor


# -------------------------------
# 3. CONECTAR AO SERVIDOR
# -------------------------------

clientSocket.connect((host, porta))
print("Ligado ao servidor!")

# -------------------------------
# 4. ENVIAR MENSAGEM AO SERVIDOR
# -------------------------------
# encode() converte string para bytes
while True:
    mensagem = input("Escreva a sua mensagem (digite Sair para sair): ")
    clientSocket.send(mensagem.encode())
    if mensagem.lower() == "sair":
        print("Conexões fechadas.")
        clientSocket.close()
        break
    resposta = clientSocket.recv(1024).decode()
    print("Resposta do servidor:", resposta)
    

# -------------------------------
# 5. RECEBER RESPOSTA DO SERVIDOR
# -------------------------------
# recv(1024) -> recebe até 1024 bytes
# decode() -> converte bytes para string




# -------------------------------
# 6. ESPERA (opcional)
# -------------------------------

time.sleep(2)


# -------------------------------
# 7. FECHAR A CONEXÃO
# -------------------------------

#clientSocket.close()
#print("Conexão fechada.")