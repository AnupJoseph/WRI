import pandas as pd
import xlsxwriter

excel = pd.read_excel(r'excels\Mar 2019-18-21 (1).xlsx',sheet_name=0,engine='xlrd')

print(excel)