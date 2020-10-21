from pdf_to_excel import PdfToExcel


def main():
    pdf = PdfToExcel('150820.pdf')
    print(getattr(pdf, 'dataframe'))


if __name__ == "__main__":
    main()
