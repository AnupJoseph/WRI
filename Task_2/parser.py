import pandas as pd
import warnings
warnings.filterwarnings('ignore')

pd.set_option("display.max_rows", None, "display.max_columns", None)


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
        combination.at[2, 'Details'] = 'Hydro-electricity'
        self.outframe = pd.concat([self.outframe, combination])

    def ppn_parser(self,):
        ppn = self.dataframe.loc[self.dataframe['Details'].str.contains(
            'PPN') | self.dataframe['Details'].str.contains('ABAN')]
        self.outframe =  pd.concat([self.outframe, ppn])

    def cpp_parser(self,):
        cpp = self.dataframe.loc[self.dataframe['Details'].str.contains('CPP') | self.dataframe['Details'].str.contains('Captive')]
        cpp.index = range(3)
        cpp.at[2,'Details'] = 'CPP - Wheeling'
        cpp.reset_index()
        self.outframe =  pd.concat([self.outframe, cpp])
    
    def non_conventional(self, ):
        non_conv = self.dataframe.loc[self.dataframe['Details'].str.contains('Bio mass')]
        print([non_conv.iloc[:,0].str.split('\n')])

    def power_purchase_total_parser(self,):
        power_total = self.dataframe.loc[self.dataframe['Details'].str.contains(
            'MTOA') | self.dataframe['Details'].str.contains('Total')]
        self.outframe =  pd.concat([self.outframe, power_total])

    def parse(self, ):
        self.hydro_thermal_gas_parser()
        self.ppn_parser()
        self.cpp_parser()

        self.power_purchase_total_parser()
        dataframe = self.outframe.copy()
        return dataframe
