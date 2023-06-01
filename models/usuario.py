class Usuario:
    def __init__(self, matricula, nome, curso, email, vinculo):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        self.email = email
        self.vinculo = vincu

    def getMatricula(self):
        return self.matricula

    def setMatricula(self, matricula):
        self.matricula = matricula
