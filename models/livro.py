class Livro:
    def __init__(self, id_livro, nome, setor, autor, quantidade_pag, area_id_area):
        self.id_livro = id_livro
        self.nome = nome
        self.setor = setor
        self.autor = autor
        self.quantidade_pag = quantidade_pag
        self.area_id_area = area_id_area 

    def getId_livro(self):
        return self.id_livro

    def setId_livro(self, id_livro):
        self.id_livro = id_livro
