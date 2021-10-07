import socket as sk
# A mesma importação feita para o cliente-udp também é feita no servidor

udp = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
# Também é instanciado um objeto com a (sub) clasee socket para dizer o tipo de conexão desejada

destiny = '',6000
# Uma tupla contendo o host e a porta par que a conexão seja feita
# No servidor não é necessário informar o host

udp.bind(destiny)
# Faz com que as informações seja jogadas para o socket...
# Dizendo aonde ele vai se conectar nesse socket

print("Servidor iniciado!\n")

while True:

    message,client = udp.recvfrom(1024)
    # Essas duas variaveis vão conter os seguintes valores
    # Message = os bytes enviados pelo cliente
    # Cliente = o endereço do cliente
    # o metodo recvfrom() é utilizado para dizer o tamanho da mensagem que pode ser recebida pelo socket udp

    if (message == bytes('Desligar servidor', 'utf-8')):
        print('Servidor sendo finalizado...')
        exit()
    else:
        print(f'Mensagem recebida de {client}\nContéudo:{message}')

udp.close()
