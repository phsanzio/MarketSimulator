from socket import *
import pickle

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
initial_sentence = input('\033[1;35mDigite 1 para começar...\033[0m')
clientSocket.send(initial_sentence.encode())
server_sentence = clientSocket.recv(1024).decode()
print(server_sentence)

def list_products(dict):
    print('\n\033[1;34m------------------------')
    print('Lista de produtos:')
    for product, price in dict.items():
            print(f'{product} - {price[0]}: R${price[1]}')
    print('------------------------\033[0m\n')

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
            if server_sentence == 'Produto não existe!':
                print('\033[1;31m' + server_sentence + '\033[0m')
            else:    
                print('\033[1;32m' + server_sentence + '\033[0m')
            break
        case 3:
            clientSocket.send(client_sentence.encode())
            server_sentence = clientSocket.recv(1024).decode()
            print(server_sentence)
            product_offer = input('Digite: ')
            clientSocket.send(product_offer.encode())
            server_sentence = clientSocket.recv(1024).decode()
            if product_offer not in received_dict.keys():
                print('\033[1;31m' + server_sentence + '\033[0m')
                break
            print('\033[1;34m' + f'{product_offer} - {received_dict[product_offer][0]}: R${received_dict[product_offer][1]}' + '\033[0m')
            print(server_sentence)
            price_want_buy = input('Digite: ')
            clientSocket.send(price_want_buy.encode())
            server_sentence = clientSocket.recv(1024).decode()
            contador = 0
            while server_sentence == 'Oferta recusada!':
                print('\033[1;31m' + server_sentence + ' Tente novamente...' + '\033[0m')
                client_sentence = input('Pressione 1 para continuar...')
                clientSocket.send(client_sentence.encode())
                server_sentence = clientSocket.recv(1024).decode()
                print('\033[1;33m' + server_sentence + '\033[0m')
                agree_deny = input('Digite: ')
                if agree_deny.lower() == 's':
                    clientSocket.send(agree_deny.encode())
                    server_sentence = clientSocket.recv(1024).decode()
                    print('\033[1;32m' + server_sentence + '\033[0m')
                    exit() #mudar
                else:
                    clientSocket.send(agree_deny.encode())
                    server_sentence = clientSocket.recv(1024).decode()
                    if contador == 4:
                        print('\033[1;31m' + server_sentence + '\033[0m')
                        exit()
                    else: 
                        print(server_sentence)
                        price_want_buy = input('Digite: ')
                        clientSocket.send(price_want_buy.encode())
                        server_sentence = clientSocket.recv(1024).decode()
                contador+=1

            print('\033[1;32m' + server_sentence + '\033[0m')
            break
        case 4:
            clientSocket.send(client_sentence.encode())
            break

clientSocket.close()