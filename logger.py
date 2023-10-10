import datetime

class Logger:
    def __init__(self):
        self.log_file = open("robo-log.txt", "a")  # Abre o arquivo para escrita (append)

    def log(self, mensagem):
        agora = datetime.datetime.now()
        log_mensagem = f"[{agora}] (Log): {mensagem}\n"
        print(log_mensagem, end='')  # Exibe no console
        self.log_file.write(log_mensagem)  # Escreve no arquivo

    def logErro(self, mensagem):
        agora = datetime.datetime.now()
        log_mensagem = f"[{agora}] (ERRO): {mensagem}\n"
        print(log_mensagem, end='')  # Exibe no console
        self.log_file.write(log_mensagem)  # Escreve no arquivo

    def __del__(self):
        self.log_file.close()  # Fecha o arquivo quando a instância é destruída