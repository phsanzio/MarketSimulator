from socket import *
import pickle

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
initial_sentence = input('Digite 1 para começar... ')
clientSocket.send(initial_sentence.encode())
server_sentence = clientSocket.recv(1024).decode()
print(server_sentence)

def list_products(dict):
    print('\n\033[1;34m--------------------')
    print('Lista de produtos:')
    for product, price in dict.items():
            print(f'{product.capitalize()}: R${price}')
    print('--------------------\033[0m\n')

while True:
    client_sentence = input('Digite: ')
    match int(client_sentence):
        case 1:
            clientSocket.send(client_sentence.encode())
            server_sentence = clientSocket.recv(1024)
            received_dict = pickle.loads(server_sentence)
            list_products(received_dict)
            return_menu = input('Digite 1 para ir ao menu: ')
            clientSocket.send(return_menu.encode())
            server_sentence = clientSocket.recv(1024).decode()
            print(server_sentence)
        case 2:
            clientSocket.send(client_sentence.encode())
            server_sentence = clientSocket.recv(1024).decode()
            print(server_sentence)
            product_buy = input('Digite: ')
            clientSocket.send(product_buy.encode())
            server_sentence = clientSocket.recv(1024).decode()
            print(server_sentence)
            break
        case 3:
            clientSocket.send(client_sentence.encode())
            server_sentence = clientSocket.recv(1024).decode()
            print(server_sentence)
            product_offer = input('Digite: ')
            clientSocket.send(product_offer.encode())
            server_sentence = clientSocket.recv(1024).decode()
            print(server_sentence)
            price_want_buy = input('Digite: ')
            clientSocket.send(price_want_buy.encode())
            server_sentence = clientSocket.recv(1024).decode()
            contador = 0
            while server_sentence == 'Oferta recusada!':
                print(server_sentence + ' Tente novamente...')
                client_sentence = input('Pressione 1 para continuar...')
                clientSocket.send(client_sentence.encode())
                server_sentence = clientSocket.recv(1024).decode()
                print(server_sentence)
                agree_deny = input('Digite: ')
                if agree_deny.lower() == 's':
                    clientSocket.send(agree_deny.encode())
                    server_sentence = clientSocket.recv(1024).decode()
                    print(server_sentence)
                    exit() #mudar
                else:
                    clientSocket.send(agree_deny.encode())
                    server_sentence = clientSocket.recv(1024).decode()
                    if contador == 4:
                        print(server_sentence)
                        exit()
                    else: 
                        print(server_sentence)
                        price_want_buy = input('Digite: ')
                        clientSocket.send(price_want_buy.encode())
                        server_sentence = clientSocket.recv(1024).decode()
                contador+=1

            print(server_sentence)
            break
        case 4:
            clientSocket.send(client_sentence.encode())
            break

clientSocket.close()