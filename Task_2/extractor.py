import camelot
import pandas as pd


class Extractor(object):
    def __init__(self, filename=".": str):
        self.filename = filename

    def _clean_names(self, name="": str) -> str:
        name = list(name for name in name.split('\n'))
        return '_'.join(name)

    def extract_dataframe(self) -> pd.DataFrame:
        tables = camelot.read_pdf(filepath, split_text=True, line_scale=10, shift_text=[
                                  ''], layout_kwargs={'detect_vertical': False})

        first_table = tables[0].df
        names = first_table.iloc[0].to_list()
        cleaned_names = pd.Series(map(self._clean_names, names))
        first_table = first_table.rename(columns=cleaned_names,)
        first_table.drop(first_table.index[0], inplace=True)

        return first_table
