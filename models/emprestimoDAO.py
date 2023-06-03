class EmprestimoDAO:
    def __init__(self, con):
        self.con = con

    def inserir(self, emprestimo):

        try:
            sql = "INSERT INTO emprestimo (id_exemplar, usuario_matricula, emprestimo_id, data_emprestimo, data_devolucao) VALUES (%s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (emprestimo.id_exemplar, emprestimo.usuario_matricula, emprestimo.emprestimo_id, emprestimo.data_devolucao, emprestimo.data_devolucao))

            self.con.commit()
            id_exemplar = cursor.lastrowid
            return id_exemplar

        except:
            return 0

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