class Livro:
    def __init__(self, nome, autor, quantidade_pag, area_id_area, link_capa):
        self.nome = nome
        self.autor = autor
        self.quantidade_pag = quantidade_pag
        self.area_id_area = area_id_area
        self.link_capa = link_capa

    def getId_livro(self):
        return self.id_livro

    def setId_livro(self, id_livro):
        self.id_livro = id_livro
