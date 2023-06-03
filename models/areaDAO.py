class AreaDAO:
    def __init__(self, con):
        self.con = con

    def listar_area(self, nome=None):
        try:
            cursor = self.con.cursor()
            if nome is not None:
                # pegar somente um produto
                sql = "SELECT * FROM Area WHERE nome=%s"
                cursor.execute(sql, (nome))
                area = cursor.fetchone()
                return area
            else:
                # pegar todas os produtos
                sql = "SELECT * FROM Area"
                cursor.execute(sql)
                areas = cursor.fetchall()
                return areas 

        except:
            return None