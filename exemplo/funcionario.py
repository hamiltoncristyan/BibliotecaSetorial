class Funcionario:
    def __init__(self, nome, num_telefone, email, senha, tipo):
        self.nome = nome
        self.num_telefone = num_telefone
        self.email = email
        self.senha = senha
        self.tipo = tipo

    def getMatricula(self):
        return self.matricula

    def setMatricula(self, matricula):
        self.matricula = matricula

    def getSenha(self):
        return self.senha

    def setSenha(self, senha):
        self.senha = senha
