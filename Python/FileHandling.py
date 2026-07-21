import csv
import json

with open ('sample.csv') as f:
    f_csv = csv.reader(f)

headers = ['Symbol','Price','Date','Time','Change','Volume']

rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
 ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
 ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
]

print(rows)



data = {
 'name' : 'ACME',
 'shares' : 100,
 'price' : 542.23
}

with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)







