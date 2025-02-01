##ML JSON CONVERTER


#CSV

import csv
import json

data = {}

with open('Meteorite_Landings.json', 'r') as f:
    data = json.load(f)

with open('Meteorite_Landings.csv', 'w') as o:
    csv_dict_writer = csv.DictWriter(o, data['meteorite_landings'][0].keys())
    csv_dict_writer.writeheader()
    csv_dict_writer.writerows(data['meteorite_landings'])


#XML

import json
import xmltodict


import json
import xmltodict


data = {}
data['meteorite_landings'] = []

with open('Meteorite_Landings.json', 'r') as f:
    json_data = json.load(f)
    json_data['meteorite_landings']


root = {}
root['data'] = data

with open('Meteorite_Landings.xml', 'w') as o:
    o.write(xmltodict.unparse(root, pretty=True))


#YAML

import yaml

with open('Meteorite_Landings.json', 'r') as f:
    meteorite_data = json.load(f)

data = {}
data['meteorite_landings'] = meteorite_data['meteorite_landings']



with open('meteorite_landings.yaml', 'w') as o:
    yaml.dump(data, o)

