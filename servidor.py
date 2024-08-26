from socket import *
import pickle
import random

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
price_sell = {'arroz': '20.00', 'frango':'18.00', 'alface':'2.00'}
price_paid = {'arroz': '12.00', 'frango':'10.00', 'alface':'0.20'}
connectionSocket, addr = serverSocket.accept()
initial_sentence = connectionSocket.recv(1024).decode()
connectionSocket.send('1 - Listar produtos'.encode())
print("O cliente conectou ao servidor...")

def menu():
    connectionSocket.send('1 - Listar produtos\n2 - Comprar\n3 - Fazer oferta\n4 - Sair'.encode())

def oferta(product):
    contador = 0
    price = float(price_sell[product])
    price_acceptable = float(price_paid[product]) * 1.3
    temp_price = 0
    connectionSocket.send('Informe o preço que deseja pagar...'.encode())
    while contador < 5:
        price_want_buy = connectionSocket.recv(1024).decode()
        if contador > 0:
            while random_price >= temp_price:
                random_price = random.uniform(price_acceptable, price)
            temp_price = random_price
        else:
            random_price = random.uniform(price_acceptable, price)
            temp_price = random_price
        if float(price_want_buy) < random_price:
            connectionSocket.send('Oferta recusada!'.encode())
            client_continue = connectionSocket.recv(1024).decode()
            contra_offer = 'Contraoferta: R${:.2f}\nVocê aceita (s/n)?'.format(random_price)
            connectionSocket.send(contra_offer.encode())
            agree_deny = connectionSocket.recv(1024).decode()
            if agree_deny.lower() == 's':
                connectionSocket.send('Compra realizada! Volte sempre!'.encode())
                print(f'O cliente efetuou a compra de {product.lower().capitalize()}...')
                break
            else:
                if contador == 4:
                    connectionSocket.send('Tentativas Excedidas!'.encode())
                    print('Cliente excedeu as tentativas!')
                    break
                else:
                    connectionSocket.send('Informe uma nova oferta...'.encode())
        else:
            print('Valor que seria fornecido: R${:.2f}\nValor pago pelo cliente: R${}'.format(random_price, price_want_buy))
            connectionSocket.send('Oferta aceita e compra realizada! Volte sempre!'.encode())
            print(f'O cliente efetuou a compra de {product.lower().capitalize()}...')
            break
        contador+=1
            

while True:
    client_sentence = connectionSocket.recv(1024).decode()
    match int(client_sentence):
        case 1:
            connectionSocket.send(pickle.dumps(price_sell))
            connectionSocket.recv(1024).decode()
            menu()
        case 2:
            connectionSocket.send('Informe o nome do produto que deseja comprar...'.encode())
            product_buy = connectionSocket.recv(1024).decode()
            if product_buy.lower() in price_sell.keys():
                connectionSocket.send('Compra realizada! Volte sempre!'.encode())
                print(f'O cliente efetuou a compra de {product_buy.lower().capitalize()}...')
            else:
                connectionSocket.send('Produto não existe!'.encode())
                print(f'O cliente não conclui a compra de {product_buy.lower().capitalize()}...')
            print("O cliente desconectou do servidor...")
            break
        case 3:
            connectionSocket.send('Informe o nome do produto que deseja comprar...'.encode())
            product_offer = connectionSocket.recv(1024).decode()
            if product_offer.lower() in price_sell.keys():
                oferta(product_offer)
            else:
                connectionSocket.send('Produto não existe!'.encode())
                print(f'O cliente não conclui a compra de {product_offer.lower().capitalize()}...')
            print("O cliente desconectou do servidor...")
            break
        case 4:
            print("O cliente desconectou do servidor...")
            break


connectionSocket.close()
serverSocket.close()