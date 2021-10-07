from http.client import HTTPConnection, ResponseNotReady
# Diferente do servidor Http é utilizado uma classe diferente para fazer esse trabalho de cliente no http

connection = HTTPConnection('localhost',7000)
# Aqui é instanciado um objeto com as informações de aonde o cliente deve se conectar

connection.request("GET","/")
# Com esse metodo é possivel dizer o tipo de requisição que o cliente está pedindo...
# e o caminho dessa requisição, nesse caso é a raiz ("/")

response = connection.getresponse()
# Aqui jogaremos a requisição enviada pelo servidor para essa variavel

page = response.read()
# O metodo .read() irá ler a mensagem e devolver o corpo do http que foi enviado pelo servidor

print(page)
# E um print para monstrar a pagina no console(cmd)


# Por algum motivo o programa pode dar erro na hora de acessar o servidor (isso ocorreu no meu navegador padrão que eu uso que seria o brave)
# porém esse erro não aconteceu no navegador Microsoft Egde