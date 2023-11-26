class UsuarioDAO:
    def __init__(self, con):
        self.con = con

    def inserir(self, usuario):

        try:
            sql = "INSERT INTO usuario(matricula, nome, curso, email, vinculo, link_foto) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (
            usuario.matricula, usuario.nome, usuario.curso, usuario.email, usuario.vinculo, usuario.link_foto))

            self.con.commit()
            matricula = cursor.lastrowid
            return matricula

        except:
            return 0

    def verificar_matricula(self, matricula):
        try:
            sql = "SELECT * FROM Usuario WHERE matricula = %s"

            cursor = self.con.cursor()
            cursor.execute(sql, (matricula))

            user_data = cursor.fetchone

            return user_data is not None

        except:
            return None

    def listar_usuario(self, nome=None):
        try:
            cursor = self.con.cursor()
            if nome is not None:
                # Pegar todos os usuários
                sql = "SELECT * FROM Usuário WHERE nome = %s"
                cursor.execute(sql, (nome))
                usuario = cursor.fetchone()
                return usuario
            else:
                # pegar todos os Usuários
                sql = "SELECT * FROM Usuário"
                cursor.execute(sql)
                usuarios = cursor.fetchall()
                return usuarios

        except:
            return None
