import paho.mqtt.client as mqtt
# Diferente da biblioteca socket utilizada no TCP e UDP, na conexão mqtt é utilizada uma biblioteca diferente...
# sendo ela a paho-mqtt
import json

mqtt_sub = mqtt.Client('sub-1')
# Objeto instanciado para que esse sub seja identificado com um nome no broker

mqtt_sub.connect('localhost',port=1883)
# Metodo utilizado para que esse sub se conecte ao broker atrávez das informações dentro do metodo
mqtt_sub.subscribe('fabrica1/portao3')
# O metodo subscribe diz qual o topico que este subscriber ouvirá enquanto o programa estiver funcionando

def callback_message(client, userdata, message):
    mensagem = json.loads(message.payload.decode('utf-8'))
    # A variavel mensagem servirá para que toda informação recebida...
    # seja convertida de .json para dict...
    # assim ficando mais facil para o python entender as informações recebidas pelo broker
    if(mensagem["status"]== True):
        # já que a variavel mensagem está em forma de dict, fica facil analizar a informação recebida pelo broker
        # então fica bem mais facil fazer uma estrutura de decisão com a informação recebida
        print('Abrindo portão.')
    elif(mensagem["Status"]== False):
        print('Fechando portão.')
    else:
        pass

mqtt_sub.on_message = callback_message
# Sempre que uma mensagem for enviada ao topico escolhido pelo sub...
# ele fará um callback chamando a função callback_message para que o programa possa decidir o que fazer com o dado recebido

mqtt_sub.loop_forever()
# Este metodo fará o mesmo papel do "While True:" nas outras conexões, fazendo que o programa fique rodando direto.

