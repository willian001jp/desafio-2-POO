# TODO: Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos, 'nome' e 'saldo':
# TODO: Crie um método 'verificar_saldo' para verificar o saldo do plano sem acessar diretamente o atributo:    
# TODO: Crie um método 'mensagem_personalizada' para gerar uma mensagem personalizada com base no saldo: 

class PlanoTelefone():

    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def verificar_saldo(self):
        return self.saldo    
    
    def mensagem_personalizada(self):
        saldo = self.verificar_saldo()
        if saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."

        elif saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."

        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."


# Classe UsuarioTelefone:
class UsuarioTelefone:

    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

    def verificar_saldo(self):
        saldo_usuario = self.plano.verificar_saldo()
        mensagem_usuario = self.plano.mensagem_personalizada()
        return saldo_usuario, mensagem_usuario
# TODO: Crie um método para verificar o saldo do usuário e gerar uma mensagem personalizada:
        
# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input("nome: ")
nome_plano = input("plano: ")
saldo_inicial = float(input("saldo: "))

 # Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)  


# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()  
print(mensagem_usuario)