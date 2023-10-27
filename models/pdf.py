class pdf:
    def __init__(self, nome, autor, quantidade_pag, area_id_area, pdfcol):
        self.nome = nome
        self.autor = autor
        self.quantidade_pag = quantidade_pag
        self.area_id_area = area_id_area
        self.pdfcol = pdfcol

    def getId_Pdf(self):
        return self.id_pdf

    def setId_Pdf(self, id_pdf):
        self.id_pdf = id_pdf

