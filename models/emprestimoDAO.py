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

    def emprestimos(self, usuario_matricula):

        sql = "SELECT INTO * emprestimo WHERE usuario_matricula = %s "
        cursor = self.con.cursor()
        cursor.execute(sql, (usuario_matricula,))

        self.con.commit()
        emprestimos = cursor.fetchone
        return emprestimos


    #def autenticar(self, id_exemplar):
        #try:
            #sql = "SELECT * FROM Emprestimo WHERE id_exemplar=%s AND senha=%s"

            #cursor = self.con.cursor()
            #cursor.execute(sql, (email, senha))

            #funcionario = cursor.fetchone()  # lastrowid, fetchone, fetchall
            #return funcionario
        #except:
            #return None

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