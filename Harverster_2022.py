import requests
import csv
from datetime import datetime
import time

url = 'https://danepubliczne.imgw.pl/api/data/hydro'

response = requests.get(url)
json_resp = response.json()

#starting_time = datetime(2022, 8, 26)
now = datetime.now().strftime("%d.%m.%Y")


def get_file_name():
    file_name = '25.08.2022.csv'
    if file_name != now:
        file_name = str(now) + '.csv'
        return file_name
    else:
        return 'Error'




while True:

    print(now, ' response: ', response.status_code)

    with open(get_file_name(), 'a', encoding='utf-8', errors='ignore', newline='') as file:
        river_writer = csv.writer(file)
        river_writer.writerow(['Date', 'River', 'Station', 'Level'])

        for each in json_resp:
            river = each['rzeka']
            station = each['stacja']
            level = each['stan_wody']
            date_time = each['stan_wody_data_pomiaru']
            river_writer.writerow([date_time, river, station, level])

        file.close()

    time.sleep(10)

