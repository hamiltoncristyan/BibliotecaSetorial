from datetime import datetime, timedelta
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

    def listar_emprestimo(self):
        cursor = self.con.cursor()
        sql = "SELECT * FROM Emprestimo"
        cursor.execute(sql)
        emprestimos = cursor.fetchall()
        return emprestimos


    def listar_emprestimo_pendente(self):
        cursor = self.con.cursor()
        sql = "SELECT * FROM Emprestimo WHERE estado = 'Pendente'"
        cursor.execute(sql)
        emprestimos = cursor.fetchall()
        return emprestimos


    def listar_emprestimo_aprovado(self):
        cursor = self.con.cursor()
        sql = "SELECT * FROM Emprestimo WHERE estado = 'Aprovado'"
        cursor.execute(sql)
        emprestimos = cursor.fetchall()
        return emprestimos


    def meus_emprestimos(self, usuario_matricula):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM EMPRESTIMO WHERE usuario_matricula = %s"
            cursor.execute(sql, (usuario_matricula,))
            emprestimos = cursor.fetchall()
            return emprestimos
        except:
            return 0


    def aprovar_emprestimo(self, id_emprestimo):

        try:
            cursor = self.con.cursor()
            sql = "UPDATE EMPRESTIMO SET estado = 'Aprovado' WHERE id_emprestimo=%s"
            cursor.execute(sql, (id_emprestimo,))
            self.con.commit()
            emprestimo = cursor.fetchone()
            return emprestimo

        except:
            return 0

    def devolver_emprestimo(self, id_emprestimo):

        try:
            cursor = self.con.cursor()
            sql = "UPDATE EMPRESTIMO SET estado = 'Devolvido' WHERE id_emprestimo=%s"
            cursor.execute(sql, (id_emprestimo,))
            self.con.commit()
            emprestimo = cursor.fetchone()
            return emprestimo

        except:
            return 0

    def adiar_emprestimo(self, id_emprestimo):
        try:
            cursor = self.con.cursor()
            # Recupera a próxima linha de resultado
            cursor.execute("SELECT data_devolucao FROM EMPRESTIMO WHERE id_emprestimo = %s", (id_emprestimo,))
            data_devolucao_atual = cursor.fetchone()[0]

            nova_data_devolucao = data_devolucao_atual + timedelta(days=15)
            sql = "UPDATE EMPRESTIMO SET data_devolucao = %s WHERE id_emprestimo=%s"
            cursor.execute(sql, (nova_data_devolucao, id_emprestimo))
            self.con.commit()

        except:
            return 0
