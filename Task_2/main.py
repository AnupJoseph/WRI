import os
import sys
import fire

from converter import PdfToExcel
from parser import ExcelParser


class Controller():

    def transform(self, file):

        pdf = PdfToExcel(file)
        exp = ExcelParser(pdf.dataframe)
        extracted_data = exp.parse()
        print(extracted_data)

    def parse(self, data='./data'):
        for files in os.listdir(data):
            self.transform(f"{data}/{files}")


if __name__ == "__main__":
    fire.Fire(Controller)
