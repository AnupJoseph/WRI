from converter import PdfToExcel
from parser import ExcelParser

def transformer(file):
    pdf = PdfToExcel('150820.pdf')
    # print(getattr(pdf, 'dataframe'))
    exp = ExcelParser(pdf.dataframe)
    extracted_data = exp.parse()
    print(extracted_data)

def main():
    transformer('150820.pdf')

if __name__ == "__main__":
    main()
