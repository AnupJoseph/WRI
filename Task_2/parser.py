import pandas as pd
import warnings
warnings.filterwarnings('ignore')


def simple_drops(dataframe):
    dataframe = dataframe.drop(dataframe.columns[0], axis=1)
    dataframe = dataframe.drop(dataframe.index[0], axis=0)
    return dataframe


class ExcelParser(object):

    def __init__(self, dataframe):
        self.dataframe = simple_drops(dataframe)
        self.outframe = pd.DataFrame()

    def hydro_thermal_gas_parser(self, ):
        combination = self.dataframe.loc[self.dataframe['Details'].str.contains(
            'Hydro') | self.dataframe['Details'].str.contains('Thermal') | self.dataframe['Details'].str.contains('Gas')]
        combination.at[2,'Details'] = 'Hydro-electricity'
        self.outframe = pd.concat([self.outframe, hydro])

    def thermal_parser(self, ):

    def parse(self, ):
        self.hydro_parser()
        dataframe = self.outframe.copy()
        return dataframe
