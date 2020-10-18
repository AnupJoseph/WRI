def clean_names(name):
    name = list(name for name in name.split('\n'))
    return '_'.join(name)


def create_excel(filepath='.'):
    import os
    import xlsxwriter
    import pandas as pd

    if not os.path.exists('excels'):
        os.makedirs('excels')
    excel_file_path = filepath[:-4] + ".xlsx"
    tables = camelot.read_pdf(filepath, split_text=True, line_scale=10, shift_text=[
                              ''], layout_kwargs={'detect_vertical': False})
    first_table = tables[0].df

    names = first_table.iloc[0].to_list()
    cleaned_names = pd.Series(map(clean_names, names))
    first_table = first_table.rename(columns=cleaned_names,)
    first_table.drop(first_table.index[0], inplace=True)

    writer = pd.ExcelWriter(
        f'excels/extracted_{excel_file_path}', engine='xlsxwriter')
    first_table.to_excel(writer, index=False, sheet_name='report')
    writer.save()
    return first_table


def hydro_parser(input_dataframe, outframe):
    hydro = input_dataframe.loc[input_dataframe['Details'].str.contains(
        'Hydro')]
    hydro.loc[:, 'Details'] = 'Hydro'
    return pd.concat([hydro, outframe])


def thermal_gas_parser(input_dataframe, outframe):
    thermal_gas = input_dataframe.loc[input_dataframe['Details'].str.contains(
        'Thermal') | input_dataframe['Details'].str.contains('Gas')]
    return pd.concat([outframe, thermal_gas])


def ppn_parser(input_dataframe, outframe):
    ppn = input_dataframe.loc[input_dataframe['Details'].str.contains(
        'PPN') | input_dataframe['Details'].str.contains('ABAN')]
    return pd.concat([outframe, ppn])


def cpp_parser(input_dataframe, outframe):
    cpp = input_dataframe.loc[input_dataframe['Details'].str.contains('CPP')]
    cpp.loc[cpp['Details'].str.contains('Third')]['Details'] = 'CPP'
    cpp.fillna(value=0, inplace=True)
    return pd.concat([outframe, cpp])


def non_conventional_parser(input_dataframe, outframe):
    non_conventional = input_dataframe.loc[input_dataframe['Details'].str.contains(
        'Bio mass')]
    temp_frame = pd.DataFrame(columns=input_dataframe.columns)

    details = non_conventional.iloc[:, 0].str.split('\n').tolist()
    details[0].pop(-1)
    details[0].pop(-2)
    temp_frame[input_dataframe.columns[0]] = pd.Series(details[0])

    lighting_peak = non_conventional.iloc[:, 2].str.split('\n').tolist()
    temp_frame[input_dataframe.columns[2]] = lighting_peak[0]

    minimum_load = non_conventional.iloc[:, 3].str.split('\n').tolist()
    temp_frame[input_dataframe.columns[3]] = minimum_load[0]

    morning_peak = non_conventional.iloc[:, 4].str.split('\n').tolist()
    temp_frame[input_dataframe.columns[4]] = morning_peak[0]

    consumption = non_conventional.iloc[:, 5].str.split().tolist()
    consumption[0].append(0)
    consumption[0].append(0)
    temp_frame[input_dataframe.columns[5]] = consumption[0]

    temp_frame.fillna(value=0, inplace=True)
    return pd.concat([outframe, temp_frame])


def wind_solar_parser(input_dataframe, outframe):
    wind_solar = input_dataframe.loc[input_dataframe['Details'].str.contains(
        'Wind') | input_dataframe['Details'].str.contains('Solar')]
    temp_frame = pd.DataFrame(columns=input_dataframe.columns)

    details = wind_solar.iloc[:, 0].str.split('\n').tolist()
    details[0].pop(1)
    details[0].pop(2)
    temp_frame[input_dataframe.columns[0]] = pd.Series(details[0])

    lighting_peak = wind_solar.iloc[:, 2].str.split('\n').tolist()
    temp_frame[input_dataframe.columns[2]] = lighting_peak[0]

    minimum_load = wind_solar.iloc[:, 3].str.split('\n').tolist()
    temp_frame[input_dataframe.columns[3]] = minimum_load[0]

    morning_peak = wind_solar.iloc[:, 4].str.split('\n').tolist()
    temp_frame[input_dataframe.columns[4]] = morning_peak[0]

    consumption = wind_solar.iloc[:, 5].str.split().tolist()
    temp_frame[input_dataframe.columns[5]] = consumption[0]

    temp_frame.fillna(0, inplace=True)
    return pd.concat([outframe, temp_frame])


def cgs_data_parser(input_dataframe, outframe):
    cgs_capacity = input_dataframe.loc[input_dataframe['Details'].str.contains(
        'CGS')]
    return pd.concat([outframe, cgs_capacity])


def power_purchase_total_parser(input_dataframe, outframe):
    power_total = input_dataframe.loc[input_dataframe['Details'].str.contains(
        'MTOA') | input_dataframe['Details'].str.contains('Total')]
    return pd.concat([outframe, power_total])
