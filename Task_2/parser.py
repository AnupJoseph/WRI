import pandas as pd


class ExcelParser(object):

    @staticmethod
    def simple_drops(cls,dataframe):
        dataframe = dataframe.drop(dataframe.columns[0], axis=1)
        dataframe = dataframe.drop(dataframe.index[0], axis=0)
        return dataframe

    def __init__(self, dataframe):
        self.dataframe = simple_drops(dataframe)
        self.outframe = pd.DataFrame()

    def hydro_parser(self, ):
        hydro = self.dataframe.loc[self.dataframe['Details'].str.contains(
            'Hydro')]
        hydro.loc[:, 'Details'] = 'Hydro'
        self.dataframe = pd.concat([self.outframe, hydro])

    def parse(self, ):
        self.hydro_parser()
        print(self.dataframe)

        return dataframe
