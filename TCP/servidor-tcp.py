import socket as sk
#Esta mesma biblioteca utilizada na conexão udp também servirá para realizar a conexão tcp

origin = '',7000

tcp = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
# É instanciado um objeto chamado tcp que receberá esse socket(acima deste comentário)
# SocketKind SOCK_STREAM serve para realizar conexão tipo TCP

tcp.bind(origin)# Ele vincula esse endereço ao socket tcp
tcp.listen(1)# É ele diz ao socket quantas conexões podem ser aceitas antes de negar novas conexões

print("Servidor iniciado!\n")

while True:
    # Este primeiro loop servirá para garantir que o socket tpc façá uma conexão com o cliente
    conection, client = tcp.accept()# Quando uma conexão for feita este metodo retornará o Endereço do Host e a Porta
    print(f"Servidor conectado a {client}")

    while True:
        message = conection.recv(1024)#Esta variavel message irá receber o contéudo mandado pelo cliente
        if (message == bytes("Desligar servidor", encoding= 'utf-8')):
        # Um sistema de comparação para que o servidor possa ser desligado atrávez do cliente por uma mensagem especifica
            print("Servidor desligando...")
            exit()
        else:
            print(f"Mensagem do cliente: {client}.\nConteúdo: {message}.")
                
conection.close()
#Por algum motivo meu windows não permite esse tipo de conexão ser feita, então eu não consigo testar para ver se o codigo está 100% funcional