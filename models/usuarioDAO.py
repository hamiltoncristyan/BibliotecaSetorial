class UsuarioDAO:
    def __init__(self, con):
        self.con = con

    def inserir(self, usuario):

        try:
            sql = "INSERT INTO usuario(matricula, nome, curso, email, vinculo) VALUES (%s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (usuario.matricula, usuario.nome, usuario.curso, usuario.email, usuario.vinculo))

            self.con.commit()
            matricula = cursor.lastrowid
            return matricula

        except:
            return 0

    def autenticar(self, matricula):
        try:
            sql = "SELECT * FROM Usuário WHERE matricula=%s"

            cursor = self.con.cursor()
            cursor.execute(sql, (matricula))

            usuario = cursor.fetchone()  # lastrowid, fetchone, fetchall
            return usuario
        except:
            return None

    def listar_usuario(self, nome=None):
        try:
            cursor = self.con.cursor()
            if nome is not None:
                # pegar somente um produto
                sql = "SELECT * FROM Usuário WHERE nome=%s"
                cursor.execute(sql, (nome))
                usuario = cursor.fetchone()
                return usuario
            else:
                # pegar todas os produtos
                sql = "SELECT * FROM Usuário"
                cursor.execute(sql)
                usuario = cursor.fetchall()
                return usuarios

        except:
            return None