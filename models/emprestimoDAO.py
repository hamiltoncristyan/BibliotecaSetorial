class EmprestimoDAO:
    def __init__(self, con):
        self.con = con

    def inserir(self, emprestimo):

        try:
            sql = "INSERT INTO emprestimo (livro_id_livro, livro_area_id_area, usuario_matricula, data_emprestimo, data_devolucao, estado) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (emprestimo.livro_id_livro, emprestimo.livro_area_id_area, emprestimo.usuario_matricula, emprestimo.data_emprestimo, emprestimo.data_devolucao, emprestimo.estado))

            self.con.commit()
            emprestimo = cursor.lastrowid
            return emprestimo

        except:
            return 0

    def atualizar(self, livro_id_livro, estado):

        try:
            sql = "UPDATE emprestimo SET estado = %s WHERE livro_id_livro = %s"
            cursor = self.con.cursor()
            cursor.execute(sql, (estado, livro_id_livro,))

            self.con.commit()

            update = cursor.fetchone()
            return update

        except:
            return None


    def emprestimos(self, usuario_matricula):
        try:
            sql = "SELECT * FROM emprestimo WHERE usuario_matricula = %s "
            cursor = self.con.cursor()
            cursor.execute(sql, (usuario_matricula,))
            emprestimos = cursor.fetchall()
            return emprestimos
        except:
            return None

    #def autenticar(self, id_exemplar):
        #try:
            #sql = "SELECT * FROM Emprestimo WHERE id_exemplar=%s AND senha=%s"

            #cursor = self.con.cursor()
            #cursor.execute(sql, (email, senha))

            #funcionario = cursor.fetchone()  # lastrowid, fetchone, fetchall
            #return funcionario
        #except:
            #return None
    #
    # def listar_emprestimo(self, emprestimo_id=None):
    #     try:
    #         cursor = self.con.cursor()
    #         if is not None:
    #             # pegar somente um produto
    #             sql = "SELECT * FROM Emprestimo WHERE emprestimo_id=%s"
    #             cursor.execute(sql, (emprestimo_id))
    #             emprestimo = cursor.fetchone()
    #             return emprestimo
    #         else:
    #             # pegar todas os produtos
    #             sql = "SELECT * FROM Funcionario"
    #             cursor.execute(sql)
    #             emprestimos = cursor.fetchall()
    #             return emprestimos
    #
    #     except:
    #         return None