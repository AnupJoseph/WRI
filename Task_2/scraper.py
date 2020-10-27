def time_strings(start_month=1, start_date=1, end_date=15, end_month=12, year=2020):
    import datetime
    start_date = datetime.datetime(year, start_month, start_date)
    end_date = datetime.datetime(year, end_month, end_date)
    step = datetime.timedelta(days=1)

    result = []
    while start_date < end_date:
        date = str(start_date.strftime('%d%m%Y'))
        if start_date.month > 10:
            date = date[:2] + date[2:]
        date = date[:-2]
        result.append(date)
        start_date += step

    return result


def pdf_downloader(date_string=''):
    import requests
    from urllib.error import HTTPError
    import os
    if not os.path.exists('data'):
        os.makedirs('data')
    try:
        response = requests.get(
            f"http://tnebldc.org/Reports1/2020/{date_string}/peakdet.pdf")
        if response:
            print(f"Valid response downloading_pdf of {date_string}")
            with open(f"data/{date_string}.pdf", 'wb') as file:
                file.write(response.content)
    except HTTPError:
        print("Resource not found")


for _, date_string in enumerate(time_strings()):
    pdf_downloader(date_string=date_string)