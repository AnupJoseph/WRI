class PdfToExcel(object):

    def __init__(self,filename = ".": str):
        self.filename = filename
        self.dataframe = self._create_dataframe()
        

    def _create_dataframe(self):
        from extractor import Extractor
        ex = Extractor(self.filename)
        return ex.extract_dataframe()
