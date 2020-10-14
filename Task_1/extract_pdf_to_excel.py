import camelot

tables = camelot.read_pdf("Sample SLDC file.pdf")
first_table = tables[0].df
print(first_table)