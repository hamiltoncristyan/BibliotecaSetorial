class PdfDAO:
    def __init__(self, con):
        self.con = con

    def inserir(self, pdf):

        try:
            sql = "INSERT INTO pdf (nome, autor, quantidade_pag, area_id_area, pdfcol) VALUES(%s, %s, %s, %s, %s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (pdf.nome, pdf.autor, pdf.quantidade_pag, pdf.area_id_area, pdf.pdfcol))

            self.con.commit()
            id_pdf = cursor.lastrowid
            return id_pdf

        except:
            return 0

    def autenticar(self, nome):
        try:
            sql = "SELECT * FROM pdf WHERE Pdf=%s"

            cursor = self.con.cursor()
            cursor.execute(sql, (nome))

            Pdf = cursor.fetchone()  # lastrowid, fetchone, fetchall
            return Pdf
        except:
            return None

    def listar_Pdf(self):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM Pdf"
            cursor.execute(sql)
            Pdf = cursor.fetchall()
            return Pdf

        except:
            return None

    def listar_Pdf_area(self, area_id_area):
        try:
            cursor = self.con.cursor()
            if area_id_area is not None:
                sql = "SELECT * FROM Pdf WHERE area_id_area = %s"
                cursor.execute(sql, (area_id_area,))
                Pdf_area = cursor.fetchall()
                return Pdf_area
        except:
            return None

    def listar_Pdf_nome(self, nome=None):
        try:
            cursor = self.con.cursor()
            if nome is not None:
                # pegar somente um produto
                sql = "SELECT * FROM Pdf WHERE nome=%s"
                cursor.execute(sql, (nome))
                Pdf = cursor.fetchone()
                return Pdf
            else:
                # pegar todas os produtos
                sql = "SELECT * FROM Pdf"
                cursor.execute(sql)
                Pdf = cursor.fetchall()
                return Pdf

        except:
            return None

    def excluir(self, id_Pdf):
        try:
            sql = "DELETE FROM Pdf WHERE id_Pdf = %s"
            cursor = self.con.cursor()
            cursor.execute(sql, (id_Pdf,))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0
