from utils.save_pdf import save_page

# These files are automatically processed to the data/processed folder
# data_dict = {
#     '../Task_3/raw/Mar 2016.pdf':13,
#     '../Task_3/raw/Mar 2016.pdf':20,
#     '../Task_3/raw/Mar 2016.pdf':21,
#     '../Task_3/raw/Mar 2016.pdf':25,
#     '../Task_3/raw/Mar 2016.pdf':26,
# }
file_path = '../Task_3/raw/Mar 2016.pdf'
page_no = [13,20,21,25,26]

data_dict = {
    '../Task_3/raw/Mar 2016.pdf': [13,20,21,25,26],

}
def main():

    for key,value in data_dict.items():
        for page in value:
            save_page(key,page)
    # for page in page_no:
    #     save_page(file_path,page)


if __name__ == "__main__":
    main()