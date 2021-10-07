import socket as sk

destiny = 'localhost' , 7000
# Esta tupla servirá para mostrar ao cliente aonde a mensagem deverá ser enviada

tcp = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
# Socket para que o tipo de conexão tcp sejá realizado

tcp.connect(destiny)
# Fazendo com que o socket tcp criado acima se conecte no servidor

while True:
    # Um loop para que o cliente possa mandar mensagens sempre que quiser
    message = bytes(input("Digite uma mensage: "), encoding='utf-8')

    if (message == bytes("Desligar cliente", encoding= 'utf-8')):
        # Um comparador para que o cliente possa ser desligado atrávez dele mesmo
        print("Finalizando cliente!")
        exit()
    else:
        print("Mensagem enviada!\n")
        tcp.send(message)


#Por algum motivo meu windows não permite esse tipo de conexão ser feita, então eu não consigo testar para ver se o codigo está 100% funcional