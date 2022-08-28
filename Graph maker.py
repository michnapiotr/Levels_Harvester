import pandas as pd
import csv

graph_data = '26.08.2022.csv'

with open(graph_data, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    print(reader)
    f.close()