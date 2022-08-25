import requests
import csv
from datetime import datetime
import time

url = 'https://danepubliczne.imgw.pl/api/data/hydro'

response = requests.get(url)


json_resp = response.json()

now = datetime.now().strftime("%d.%m.%Y %H.%M.%S")
print(now, ' response: ', response.status_code)

while True:


    with open('rivers_levels {}.csv'.format(now), 'a', encoding='utf-8', errors='ignore', newline='') as file:
        river_writer = csv.writer(file)
        river_writer.writerow(['Date','River', 'Station', 'Level'])

        for each in json_resp:
            river = each['rzeka']
            station = each['stacja']
            level = each['stan_wody']
            date_time = each['stan_wody_data_pomiaru']
            river_writer.writerow([date_time, river, station, level])

        file.close()

    time.sleep(3600)

