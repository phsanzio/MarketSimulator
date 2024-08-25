from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
products = {'arroz': '4.00', 'frango':'5.00'}
connectionSocket, addr = serverSocket.accept()
print("O servidor esta pronto esperando mensagens")

def menu():
    connectionSocket.send('1 - Listar produtos\n2 - Fazer oferta'.encode())

def list_products(products):
    connectionSocket.send('----------------\n'.encode())
    connectionSocket.send('Lista de produtos:\n'.encode())
    for product, price in products.items():
        connectionSocket.send((f'{product.capitalize()}: R${price}\n').encode())
    connectionSocket.send('----------------\n'.encode())
        
def oferta(teste):
    #produto = connectionSocket.recv(1024).decode()
    connectionSocket.send(products[teste].encode())


menu()

while True:
    #menu()
    sentence = connectionSocket.recv(1024).decode()
    print(sentence)
    if sentence.lower() == 'sair':
        break
    else:
        if sentence == '1':
            list_products(products)
        elif sentence == '2':
            connectionSocket.send('Produto?'.encode())
            sentence = connectionSocket.recv(1024).decode()
            oferta(sentence)

connectionSocket.close()
serverSocket.close()
    # elif sentence == 2:
    #     connectionSocket.send('pito'.encode())
    # capitalizedSentence = sentence.upper()
    # teste = products.items()
    # print(teste)
    #connectionSocket.send((all_products(products)).encode())
    #connectionSocket.close()