# Para fazer uma conexão udp é necessario uma biblioteca para isso
# Sendo ela a biblioteca socket
import socket as sk 

udp = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
# Aqui é instanciado um objeto que utiliza a (sub)classe socket
# Nela temos duas intancias,AddressFamily e SocketKind
# AddressFamily serve para dizer qual familia de procotolos irá ser utilizada
# SocketKind serve para dizer qual tipo de conexão será feita (nesse caso UDP)

destiny = 'localhost', 6000
#Aqui eu crio uma tupla para que o programa saiba aonde o 
#conteúdo da mensagem deverá ser enviado 

print("Cliente iniciado!")

while True:
    # É feito um loop para que o cliente possa mandar mensagens sempre que quiser, ja que o programa ira rodar para sempre
    message = bytes(input("Digite uma mensagem: "), encoding= 'utf-8')
    # Essa variavel irá guardar um input e esse input irá receber a mensagem que o cliente digitou
    # Porém, como é uma conexão de baixo nivel a troca de informações deve ser feita atrávez de bytes
    # É necessário o encoding para que a mensagem seja codificada de tal forma para que ela seja compreendida quando chegar em outra

    if (message == bytes('Sair do programa', encoding = 'utf-8')):
        # Esse comparador serve para que o programa possa ser finalizado por um comando interno
        print("Finalizando o cliente...")
        exit()
    else:
        print(f'Mensagem para {destiny[0]}.\nNa porta {destiny[1]}.\n conteúdo: {str(message)}.')
        udp.sendto(message,destiny)
        # Esse metodo "sendto" é utilizado para enviar o...
        # conteúdo da variável message até o endereço que está na variavel destiny
    
udp.close()
