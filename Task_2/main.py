import os
import sys
import argparse

from converter import PdfToExcel,DfToCsv
from parser import ExcelParser

parser = argparse.ArgumentParser()

def transformer(file):
    
    pdf = PdfToExcel(file)
    exp = ExcelParser(pdf.dataframe)
    extracted_data = exp.parse()
    print(extracted_data)

def main():
    parser.add_argument("-d",'--data',default='./data',action='store_true',dest=data,help="Print the word in upper case letters")

    args = parser.parse_args()
    if args.data:
        for files in os.listdir(args.data):
            transformer(f"{data}/{files}")

if __name__ == "__main__":
    main()
