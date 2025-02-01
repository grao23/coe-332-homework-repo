import json

with open('Meteorite_Landings.json', 'r') as f:
    ml_data = json.load(f)



#Summary Statistics


import json

def compute_average_mass(a_list_of_dicts, a_key_string):
    total_mass = 0.
    for i in range(len(a_list_of_dicts)):
        total_mass += float(a_list_of_dicts[i][a_key_string])
    return (total_mass / len(a_list_of_dicts))

def check_hemisphere(latitude: float, longitude: float) -> str:    # type hints
    location = ''
    if (latitude > 0):
        location = 'Northern'
    else:
        location = 'Southern'
    if (longitude > 0):
        location = f'{location} & Eastern'
    else:
        location = f'{location} & Western'
    return(location)

def count_meteorite_classes(a_list_of_dicts, a_key_string):
    count_class = {}
    for i in a_list_of_dicts:
        if i[a_key_string] in count_class:
            count_class[i[a_key_string]] += 1
        else:
            count_class[i[a_key_string]] = 1
        return(count_class)



with open('Meteorite_Landings.json', 'r') as f:
    ml_data = json.load(f)

print(compute_average_mass(ml_data['meteorite_landings'], 'mass (g)'))

for row in ml_data['meteorite_landings']:
    print(check_hemisphere(float(row['reclat']), float(row['reclong'])))
print(count_meteorite_classes(ml_data['meteorite_landings'], 'recclass'))
