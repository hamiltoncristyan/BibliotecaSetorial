class ExemplarDAO:
    def __init__(self, con):
        self.con = con

    def inserir(self, exemplar):

        try:
            sql = "INSERT INTO exemplar(id_exemplar, nome, quantidade, livro_id_livro, livro_area_id_area) VALUES (%s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (exemplar.id_livro, exemplar.nome, exemplar.quantidade, exemplar.livro_id_livro, exemplar.livro_area_id_area))

            self.con.commit()
            id_exemplar = cursor.lastrowid
            return id_exemplar

        except:
            return 0

    def listar_exemplar(self, nome=None):
        try:
            cursor = self.con.cursor()
            if nome is not None:
                # pegar somente um produto
                sql = "SELECT * FROM Exemplar WHERE nome=%s"
                cursor.execute(sql, (nome))
                exemplar = cursor.fetchone()
                return exemplar
            else:
                # pegar todas os produtos
                sql = "SELECT * FROM Exemplar"
                cursor.execute(sql)
                exemplar = cursor.fetchall()
                return exemplar

        except:
            return None