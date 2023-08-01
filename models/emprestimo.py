class Emprestimo:
    def __init__(self, livro_id_livro, livro_area_id_area, usuario_matricula, data_emprestimo, data_devolucao, estado):
        self.livro_id_livro = livro_id_livro
        self.livro_area_id_area = livro_area_id_area
        self.usuario_matricula = usuario_matricula
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.estado = estado

