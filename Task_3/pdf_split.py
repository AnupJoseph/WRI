from PyPDF2 import PdfFileWriter, PdfFileReader
import fire
def get_pdf_page(file_name='raw\Mar 20218.pdf',page=17):
    with open(file_name,'rb') as target:
        input_pdf = PdfFileReader(target)
        print("Resolved the pdf")
        data = input_pdf.getPage(page)
        print("Completed getting the pdf")

    return data

def write_pdf(data,out_file_name = 'Mar_2018',page_no=17):
    output = PdfFileWriter()
    output.addPage(data)
    with open(f"{out_file_name}_{page_no}.pdf", "wb") as outputStream:
        output.write(outputStream)
        print("Completed writing file")

class Controller(object):
    def page_splitter(self,pdf_name,page_no):
        data = get_pdf_page(pdf_name,page=page_no)
        write_pdf(data,page_no=page_no)

if __name__ == "__main__":
    fire.Fire(Controller)