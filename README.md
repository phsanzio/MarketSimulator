<h1 align="center"> Market Simulator - Pedro Sanzio </h1>
<p align="center"><img src="http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge"/></p>

## :file_folder: Informações

<p>:pencil: <strong>Nome:</strong> Pedro Sanzio</p>
<p>:books: <strong>Disciplina:</strong> Redes de Computadores</p>
<p>:school: <strong>Instituição:</strong> IFMG</p>

## :page_with_curl: Descrição do projeto

O Market Simulator é um programa para implementar a comunicação ***cliente-servidor(client-server)*** via socket em Python, para exemplificar foi feito um sistema onde, o servidor possui uma lista de produtos e o cliente pode comprá-los ou fazer uma oferta com o intuito de adquirir com o preço mais baixo que o apresentado inicialmente.

## :hammer: Funcionalidades do projeto

- <strong>Funcionalidade 1:</strong> Cliente pode fazer compras pelo preço "inicial"
- <strong>Funcionalidade 2:</strong> Cliente pode fazer oferta de preço ao servidor
- <strong>Funcionalidade 3:</strong> Servidor tem capacidade de aceitar a oferta ou elaborar uma contraoferta com base em algoritmos que calculam esse preço novo que vai ser fornecido ao cliente
- <strong>Funcionalidade 4:</strong> Cliente tem até 5 chances para "entrar em acordo" com o servidor, aceitando a contraoferta feita ou oferta um valor que o servidor aceite
- <strong>Funcionalidade 5:</strong> A lista de produtos pode ser incrementada pelo lado servidor, assim como mudar os preços de venda e também os preços que foram pagos ao "fornecedor"
- <strong>Funcionalidade 6:</strong> O código pode ser adaptado para diferentes situações
- <strong>Estratégia de contraoferta do servidor:</strong> Número aleatório entre o preço mínimo de venda e o preço apresentado inicialmente, o preço mínimo é cerca de 30% de lucro em cima do preço pago ao fornecedor, caso o servidor tenha que fazer mais de uma contraoferta, ela sempre vai ser menor que a apresentada anteriormente

## :unlock: Como usar

- <strong>Passo 1:</strong> Inicie o ***servidor.py***
- <strong>Passo 2:</strong> Inicie o ***cliente.py***
- <strong>Passo 3:</strong> Prossiga pelo lado do cliente conforme o programa vai orientando via terminal
- <strong>Passo 4:</strong> Depois de estabelecer conexão com o servidor, você vai poder escolher o que deseja dentro de um menu que será apresentado
- <strong>Passo 5:</strong> Caso escolha fazer uma oferta, você tem 5 chances, se esgotarem, o programa encerra.
## :newspaper: Autores

[<img src="https://user-images.githubusercontent.com/72276805/182635128-14d5c6cb-4856-4660-b8f2-4412c2cca72b.jpg" width=202 height=202><br><sub>Pedro Sanzio</sub>](https://instagram.com/pedro_sanzio)
