import requests
import csv

url = 'https://danepubliczne.imgw.pl/api/data/hydro'

response = requests.get(url)
print(response.status_code)

json_resp = response.json()

print(json_resp)

for each in json_resp:
    river = each['rzeka']
    station = each['stacja']
    level = each['stan_wody']

    with open('river_data.csv', 'a', encoding='utf-8', errors='ignore') as file:
        river_writer = csv.writer(file)
        river_writer.writerow([river, station, level])
        file.close()
