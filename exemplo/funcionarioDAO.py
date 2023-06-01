class FuncionarioDAO:
    def __init__(self, con):
        self.con = con

    def inserir(self, funcionario):

        try:
            sql = "INSERT INTO funcionario(nome, num_telefone, email, senha, tipo) VALUES (%s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (funcionario.nome, funcionario.num_telefone, funcionario.email, funcionario.senha, funcionario.tipo))

            self.con.commit()
            matricula = cursor.lastrowid
            return matricula

        except:
            return 0

    def autenticar(self, email, senha):
        try:
            sql = "SELECT * FROM Funcionario WHERE email=%s AND senha=%s"

            cursor = self.con.cursor()
            cursor.execute(sql, (email, senha))

            funcionario = cursor.fetchone()  # lastrowid, fetchone, fetchall
            return funcionario
        except:
            return None

    def listar_funcionario(self, nome=None):
        try:
            cursor = self.con.cursor()
            if nome is not None:
                # pegar somente um produto
                sql = "SELECT * FROM Funcionario WHERE nome=%s"
                cursor.execute(sql, (nome))
                funcionario = cursor.fetchone()
                return funcionario
            else:
                # pegar todas os produtos
                sql = "SELECT * FROM Funcionario"
                cursor.execute(sql)
                funcionarios = cursor.fetchall()
                return funcionarios

        except:
            return None