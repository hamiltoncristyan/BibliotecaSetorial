class AvaliacaoDAO:
    def __init__(self, con):
        self.con = con

    def inserir(self, avaliacao):

        try:
            sql = "INSERT INTO avaliacao (nome, data, avaliacao, livro_id_livro, livro_area_id_area) VALUES (%s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (avaliacao.nome, avaliacao.data, avaliacao.avaliacao, avaliacao.livro_id_livro, avaliacao.livro_area_id_area))
            self.con.commit()
            id_exemplar = cursor.lastrowid
            return id_exemplar

        except:
            return 0

    def listar_emprestimo(self, emprestimo_id=None):
        try:
            cursor = self.con.cursor()
            if nome is not None:
                # pegar somente um produto
                sql = "SELECT * FROM Emprestimo WHERE emprestimo_id=%s"
                cursor.execute(sql, (emprestimo_id))
                emprestimo = cursor.fetchone()
                return emprestimo
            else:
                # pegar todas os produtos
                sql = "SELECT * FROM Funcionario"
                cursor.execute(sql)
                emprestimos = cursor.fetchall()
                return emprestimos

        except:
            return None
