from socket import *
import pickle

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
initial = input('Digite 1 para começar... ')
clientSocket.send(initial.encode())
server_sentence = clientSocket.recv(1024).decode()
print(server_sentence)

def list_products(dict):
    print('\n\033[1;34m--------------------')
    print('Lista de produtos:')
    for product, price in dict.items():
            print(f'{product.capitalize()}: R${price}')
    print('--------------------\033[0m\n')

while True:
    sentence = input('Digite: ')
    match int(sentence):
        case 1:
            clientSocket.send(sentence.encode())
            server_sentence = clientSocket.recv(1024)
            received_dict = pickle.loads(server_sentence)
            list_products(received_dict)
            sentence = input('Digite 1 para ir ao menu: ')
            clientSocket.send(sentence.encode())
            server_sentence = clientSocket.recv(1024).decode()
            print(server_sentence)
        case 2:
            clientSocket.send(sentence.encode())
            server_sentence = clientSocket.recv(1024).decode()
            print(server_sentence)
            sentence = input('Digite: ')
            clientSocket.send(sentence.encode())
            server_sentence = clientSocket.recv(1024).decode()
            print(server_sentence)
            break
        case 3:
            pass
        case 4:
            clientSocket.send(sentence.encode())
            break
    
    
#     server_sentence = clientSocket.recv(1024).decode()
#     print(server_sentence)

clientSocket.close()