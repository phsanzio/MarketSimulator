from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
    sentence = input('Digite: ')
    clientSocket.send(sentence.encode())
    if sentence.lower() == 'sair':
        break
    server_sentence = clientSocket.recv(1024).decode()
    print(server_sentence)

clientSocket.close()