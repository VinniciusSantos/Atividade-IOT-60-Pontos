import paho.mqtt.client as mqtt
# Biblioteca utilizada para comunicação de pub/sub

mqtt_pub = mqtt.Client("pub-1")
# Este objeto faz com que esse pub seja identificado pelo broker com esse nome ("pub-1")

mqtt_pub.connect('localhost',port=1883)
# Informações para que o pub se conecte ao broker

def callback_publish(client, userdata, result):
    print("Dado enviado.")

mqtt_pub.on_publish = callback_publish
# Callback para que quando a mensagem for enviada (com sucesso)...
# a função callback_publish seja chamada e execute o print dizendo que o dado foi enviado

status = 'false' #Variavel vazia utilizada para colocar o valor da mensagem que será enviada ao topico selecionado

while True:
    message = input("Digite 1 para abrir o portão ou 0 para fechar o portão: ")

    if(message == '0'):
        # Estrutura de decisão para que o portão seja ligado ou desligado dependendo da resposta do usuário 
        status = 'false'
    elif(message == '1'):
        status = 'true'
    else:
        print("Somente 1 e 0 são aceitos, por favor tente novamente!")


    mqtt_pub.publish('fabrica1/portao3','{ "status" : %s }' %status)
    # Nesse metodo PUBLISH, o primeiro parametro serve para dizer em qual topico essa mensagem será enviada
    # já o segundo parametro serve para colocar a mensagem em si