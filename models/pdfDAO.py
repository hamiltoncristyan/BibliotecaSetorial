class LivroDAO:
    def __init__(self, con):
        self.con = con

    def inserir(self, livro):

        try:
            sql = "INSERT INTO livro (nome, autor, quantidade_pag, area_id_area, link_capa) VALUES(%s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (livro.nome, livro.autor, livro.quantidade_pag, livro.area_id_area, livro.link_capa))

            self.con.commit()
            id_livro = cursor.lastrowid
            return id_livro

        except:
            return 0

    def autenticar(self, nome):
        try:
            sql = "SELECT * FROM Livro WHERE livro=%s"

            cursor = self.con.cursor()
            cursor.execute(sql, (nome))

            livro = cursor.fetchone()  # lastrowid, fetchone, fetchall
            return livro
        except:
            return None

    def listar_livro(self):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM Livro"
            cursor.execute(sql)
            livro = cursor.fetchall()
            return livro

        except:
            return None

    def listar_livro_area(self, area_id_area):
        try:
            cursor = self.con.cursor()
            if area_id_area is not None:
                sql = "SELECT * FROM Livro WHERE area_id_area = %s"
                cursor.execute(sql, (area_id_area,))
                livro_area = cursor.fetchall()
                return livro_area
        except:
            return None

    def listar_livro_nome(self, nome=None):
        try:
            cursor = self.con.cursor()
            if nome is not None:
                # pegar somente um produto
                sql = "SELECT * FROM Livro WHERE nome=%s"
                cursor.execute(sql, (nome))
                livro = cursor.fetchone()
                return livro
            else:
                # pegar todas os produtos
                sql = "SELECT * FROM Livro"
                cursor.execute(sql)
                livros = cursor.fetchall()
                return livros

        except:
            return None

    def excluir(self, id_livro):
        try:
            sql = "DELETE FROM Livro WHERE id_livro = %s"
            cursor = self.con.cursor()
            cursor.execute(sql, (id_livro,))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0
