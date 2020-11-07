def table_to_df(table):
    data = []

    keys = None
    for i, row in enumerate(table.rows):
        text = (cell.text for cell in row.cells)
        if i == 0:
            keys = tuple(text)
            continue
        row_data = dict(zip(keys, text))
        data.append(row_data)

    df = pd.DataFrame(data)
    return df

def save_to_excel(dataframe_list, outfolder='excels'):
    if not os.path.exists('excels'):
        os.makedirs('excels')
    writer = pd.ExcelWriter(
        'excels/Combined_table_list.xlsx', engine='xlsxwriter')
    for tables in dataframe_list:
        tables.to_excel(writer)
    print("Writing Done")
    writer.save()