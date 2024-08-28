from socket import *
import pickle
import random

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
price_sell = {
    '1': ('Arroz 2kg', '20.00'), 
    '2': ('Peito de frango 1kg','18.00'), 
    '3': ('Alface 1und','2.00'),
    '4': ('Banana 1kg','8.98'),
    '5': ('Leite 1L','4.80'),
    '6': ('Tomate 1kg','8.80'),
    '7': ('Danoninho','9.80'),
    '8': ('Kinder Ovo','19.50')
}
price_paid = {
    '1': ('Arroz 2kg', '12.00'), 
    '2': ('Peito de frango 1kg','10.00'), 
    '3': ('Alface 1und','0.20'),
    '4': ('Banana 1kg','5.60'),
    '5': ('Leite 1L','2.00'),
    '6': ('Tomate 1kg','3.80'),
    '7': ('Danoninho','5.80'),
    '8': ('Kinder Ovo','3.50')
}
connectionSocket, addr = serverSocket.accept()
initial_sentence = connectionSocket.recv(1024).decode()
connectionSocket.send('1 - Listar produtos'.encode())
print('\033[1;34mO cliente conectou ao servidor...\033[0m')

def menu():
    connectionSocket.send('1 - Listar produtos\n2 - Comprar\n3 - Fazer oferta\n4 - Sair'.encode())

def oferta(product):
    contador = 0
    price = float(price_sell[product][1])
    price_acceptable = float(price_paid[product][1]) * 1.3
    temp_price = 0
    connectionSocket.send('Informe o preço que deseja pagar...'.encode())
    while contador < 5:
        price_want_buy = connectionSocket.recv(1024).decode()
        price_want_buy = price_want_buy.replace(',', '.')
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
                print('\033[1;32m' + f'O cliente efetuou a compra de {price_sell[product][0]} por R${random_price:.2f}...' + '\033[0m')
                break
            else:
                if contador == 4:
                    connectionSocket.send('Tentativas Excedidas!'.encode())
                    print('\033[1;31mCliente excedeu as tentativas!\033[0m')
                    break
                else:
                    connectionSocket.send('Informe uma nova oferta...'.encode())
        else:
            print('Valor que seria fornecido: R${:.2f}\nValor pago pelo cliente: R${}'.format(random_price, price_want_buy))
            connectionSocket.send('Oferta aceita e compra realizada! Volte sempre!'.encode())
            print('\033[1;32m' + f'O cliente efetuou a compra de {price_sell[product][0]}...' + '\033[0m')
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
            connectionSocket.send('Informe o número do produto que deseja comprar...'.encode())
            product_buy = connectionSocket.recv(1024).decode()
            if product_buy in price_sell.keys():
                connectionSocket.send('Compra realizada! Volte sempre!'.encode())
                print('\033[1;32m' + f'O cliente efetuou a compra de {price_sell[product_buy][0]} por R${price_sell[product_buy][1]}...' + '\033[0m')
            else:
                connectionSocket.send('Produto não existe!'.encode())
                print('\033[1;31mO cliente não conclui a compra...\033[0m')
            print("\033[1;35mO cliente desconectou do servidor...\033[0m")
            break
        case 3:
            connectionSocket.send('Informe o número do produto que deseja comprar...'.encode())
            product_offer = connectionSocket.recv(1024).decode()
            if product_offer in price_sell.keys():
                oferta(product_offer)
            else:
                connectionSocket.send('Produto não existe!'.encode())
                print('\033[1;31mO cliente não conclui a compra...\033[0m')
            print("\033[1;35mO cliente desconectou do servidor...\033[0m")
            break
        case 4:
            print("\033[1;35mO cliente desconectou do servidor...\033[0m")
            break


connectionSocket.close()
serverSocket.close()