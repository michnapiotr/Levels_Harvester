import requests
import csv
from datetime import datetime
import time

url = 'https://danepubliczne.imgw.pl/api/data/hydro'

now = datetime.now().strftime("%d.%m.%Y")


def get_file_name():
    file_name = str(now) + '.csv'
    return file_name




while True:

    response = requests.get(url)
    json_resp = response.json()

    print(get_file_name(), ' response: ', response.status_code)

    with open(get_file_name(), 'a', encoding='utf-8', errors='ignore', newline='') as file:
        river_writer = csv.writer(file)
        river_writer.writerow(['Date', 'River', 'Station', 'Level'])

        for each in json_resp:
            river = each['rzeka']
            station = each['stacja']
            level = each['stan_wody']
            date_time = each['stan_wody_data_pomiaru']
            data_lst = [date_time, river, station, level]
            river_writer.writerow(data_lst)

        file.close()

    time.sleep(3500)

