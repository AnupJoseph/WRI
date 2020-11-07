import fire
from document_extractor import DocToExcel
from utils.table_utils import save_to_excel
from utils.info import plants

def runner_function(filename,table_nos,sheet_name):
    document = DocToExcel(filename)
    print(document)
    outlist = document.convert_table_to_df(table_list=table_nos)
    save_to_excel(outlist,'excels',output_file_name,sheet_name=plants)


class Controller(object):
    def extract_tables(self, filename='/content/drive/My Drive/Tariff Order 2017.docx', table_nos="",output_file_name=""):
        runner_function(filename,table_nos,output_file_name)

if __name__ == "__main__":
    fire.Fire(Controller)