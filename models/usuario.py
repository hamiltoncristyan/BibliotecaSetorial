class Usuario:
    def __init__(self, matricula, nome, curso, email, vinculo, link_foto):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        self.email = email
        self.vinculo = vinculo
        self.link_foto = link_foto


    def getMatricula(self):
        return self.matricula

    def setMatricula(self, matricula):
        self.matricula = matricula
