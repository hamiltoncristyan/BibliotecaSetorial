class AvaliacaoDAO:
    def __init__(self, con):
        self.con = con

    def inserir(self, avaliacao):

        try:
            sql = "INSERT INTO Avaliacao (nome, data, avaliacao, livro_id_livro, livro_area_id_area) VALUES (%s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (avaliacao.nome, avaliacao.data, avaliacao.avaliacao, avaliacao.livro_id_livro, avaliacao.livro_area_id_area))
            self.con.commit()
            id_avaliacao = cursor.lastrowid
            return id_avaliacao

        except:
            return 0

    def listar_avaliacao_livro(self, livro_id_livro=None):
        try:
            cursor = self.con.cursor()
            if livro_id_livro is not None:
                # pegar somente um produto
                sql = "SELECT * FROM Avaliacao WHERE livro_id_livro=%s"
                cursor.execute(sql, (livro_id_livro,))
                avaliacao = cursor.fetchall()
                return avaliacao
            else:
                # pegar todas os produtos
                sql = "SELECT * FROM Avaliacao"
                cursor.execute(sql)
                avaliacoes = cursor.fetchall()
                return avaliacoes

        except:
            return None
