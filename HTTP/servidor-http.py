from http.server import BaseHTTPRequestHandler, HTTPServer
# Assim como MQTT o HTTP também possui uma biblioteca própria para sua programação no python



class Handler_HTTP(BaseHTTPRequestHandler):
    # Dentro dessa classe iremos utilizar uma classe já pronta para fazer nosso próprio handler
    # Assim será possivel criar nossa própria pagina http personalizada atrávez dessa Classe Filho (handler)
    
    def do_GET(self):
        #Essa função irá servir para que toda vez que esse servidor for acessado ele mande uma pagina ao cliente

        self.send_response(200)
        # Este metodo é utilizado para que quando a pagina for acessada ele mande um codigo no header da pagina.
        # Nesse caso o codigo 200 significa que a requisição do site foi bem sucedida.

        self.send_header("Content-type", "text/html")
        # Esse metodo irá dizer ao cliente que fez a requisição que tipo de arquivo será enviado a ele(Indo de textos até videos)
        # Nesse caso um texto html    

        self.end_headers()
        # Fechamento do header

        # Os metodos utilizados abaixo desse comentário irão servir para escrever o código html atrávez do python
        self.wfile.write(bytes('<html><head><title>Bem vindo</title></head>','utf-8'))
        self.wfile.write(bytes('<body>','utf-8'))
        self.wfile.write(bytes('<p>Aqui está a pagina que foi utilizada no exemplo de servidor http</p>','utf-8'))
        self.wfile.write(bytes('</body></html>','utf-8'))


Server_HTTP = HTTPServer(('localhost',7000),Handler_HTTP)
# Esse objeto instanciado servirá para que o http possa iniciar o servidor
# No primeiro parâmetro estará o host e sua porta
# No segundo parâmetro está o Handler que o servidor utilizará na hora que algum cliente se conectar ao servidor

print(f"Endereço do servidor: https://localhost:7000")

Server_HTTP.serve_forever()
# Metodo para que o servidor fique levantado para sempre até que ocorra alguma interrupção

# Por algum motivo o programa pode dar erro na hora de acessar o servidor (isso ocorreu no meu navegador padrão que eu uso que seria o brave)
# porém esse erro não aconteceu no navegador Microsoft Egde