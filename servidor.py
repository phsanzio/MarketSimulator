from socket import *
import pickle

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
products = {'arroz': '4.00', 'frango':'5.00'}
connectionSocket, addr = serverSocket.accept()
initial = connectionSocket.recv(1024).decode()
connectionSocket.send('1 - Listar produtos'.encode())
print("O cliente conectou ao servidor...")

def menu():
    connectionSocket.send('1 - Listar produtos\n2 - Comprar\n3 - Fazer oferta\n4 - Sair'.encode())

# def list_products(products):
#     #connectionSocket.send('----------------\n'.encode())
#     #connectionSocket.send('Lista de produtos:\n'.encode())
#     for product, price in products.items():
#         connectionSocket.send((f'{product.capitalize()}: R${price}\n').encode())
#     #connectionSocket.send('----------------\n'.encode())
#     #menu()
        
def oferta(teste):
    #produto = connectionSocket.recv(1024).decode()
    connectionSocket.send(products[teste].encode())


while True:
    sentence = connectionSocket.recv(1024).decode()
    #sentence = int(sentence)
    match int(sentence):
        case 1:
            connectionSocket.send(pickle.dumps(products))
            connectionSocket.recv(1024).decode()
            menu()
        case 2:
            connectionSocket.send('Informe o nome do produto que deseja comprar...'.encode())
            sentence = connectionSocket.recv(1024).decode()
            if sentence.lower() in products.keys():
                connectionSocket.send('Compra realizada! Volte sempre!'.encode())
                print(f'O cliente efetuou a compra de {sentence.lower().capitalize()}...')
            else:
                connectionSocket.send('Produto não existe!'.encode())
                print(f'O cliente não conclui a compra de {sentence.lower().capitalize()}...')
            print("O cliente desconectou do servidor...")
            break
        case 3:
            pass
        case 4:
            print("O cliente desconectou do servidor...")
            break
    #menu()
    # sentence = connectionSocket.recv(1024).decode()
    # print(sentence)
    

connectionSocket.close()
serverSocket.close()
    # elif sentence == 2:
    #     connectionSocket.send('pito'.encode())
    # capitalizedSentence = sentence.upper()
    # teste = products.items()
    # print(teste)
    #connectionSocket.send((all_products(products)).encode())
    #connectionSocket.close()