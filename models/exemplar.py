class Exemplar:
    def __init__(self, id_exemplar, nome, quantidade, livro_id_livro, livro_area_id_area):
        self.id_exemplar = id_exemplar
        self.nome = nome
        self.quantidade = quantidade
        self.livro_id_livro = livro_id_livro
        self.livro_area_id_area = livro_area_id_area

    def getId_exemplar(self):
        return self.id_exemplar

    def setId_exemplar(self, id_exemplar):
        self.id_exemplar = id_exemplar