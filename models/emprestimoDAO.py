class EmprestimoDAO:
    def __init__(self, con):
        self.con = con

    def inserir(self, emprestimo):

        try:
            sql = "INSERT INTO emprestimo (livro_id_livro, livro_area_id_area, usuario_matricula, data_emprestimo, data_devolucao, estado) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (emprestimo.livro_id_livro, emprestimo.livro_area_id_area, emprestimo.usuario_matricula,
                                 emprestimo.data_emprestimo, emprestimo.data_devolucao, emprestimo.estado))

            self.con.commit()
            emprestimo = cursor.lastrowid
            return emprestimo

        except:
            return 0

    def listar_emprestimo(self, id_emprestimo=None):
        try:
            cursor = self.con.cursor()
            if id_emprestimo is not None:
                # pegar somente um produto
                sql = "SELECT * FROM Emprestimo WHERE id_emprestimo=%s"
                cursor.execute(sql, (id_emprestimo))
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
