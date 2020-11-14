from PyPDF2 import PdfFileWriter,PdfFileReader
import os

def save_page(file_name,page_number):
    with open(file_name,"rb") as pdf_file:
        print(f"Opening {file_name}")
        input_pdf = PdfFileReader(file_name)

        if not os.path.exists("data/processed/pdf"):
            os.makedirs("data/processed/pdf")
        
        output = PdfFileWriter()
        output.addPage(input_pdf.getPage(page_number))
        file_name = file_name.split("/").pop(-1).split('.').pop(-2)
        with open(f"data/processed/pdf/{file_name}_{page_number+1}.pdf",'wb') as output_file:
            print(f"Writing {page_number+1} to {file_name}_{page_number+1}.pdf")
            output.write(output_file)