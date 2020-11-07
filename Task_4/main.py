import fire
from document_extractor import DocToExcel
from utils.table_utils import save_to_excel

def runner_function(filename,table_nos):
    document = DocToExcel(filename)
    print(document)
    outlist = document.convert_table_to_df(table_list=table_nos)
    save_to_excel(outlist,'excels')


class Controller(object):
    def extract_tables(self, filename='/content/drive/My Drive/Tariff Order 2017.docx', table_nos=""):
        runner_function(filename,table_nos)

if __name__ == "__main__":
    fire.Fire(Controller)