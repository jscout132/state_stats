
from state_dict import full_state_dictionary
# from state_dict_folder.states import state_bird_list, state_capitals, state_flowers, state_population, state_govs
# from state_dict_folder.states import state_gov_party, state_land_area

print(full_state_dictionary['AL'])


def add_abbs(full_state_dictionary):
    file_path = 'state_dict.py'
    for k,v in full_state_dictionary.items():
        v.update({'gov_party':'holder'})
    with open(file_path,'w') as file:
        file.write(str(full_state_dictionary))
# add_abbs(full_state_dictionary)

def add_lat(full_state_dictionary):
    file_path = 'state_dict.py'
    for k,v in full_state_dictionary.items():
        v.update({'lat':'holder'})
        v.update({'lon':'holder'})
    with open(file_path,'w') as file:
        file.write(str(full_state_dictionary))
add_lat(full_state_dictionary)


# adding state names to dictionary
def update_state_info(state_names, state_dict):
    file_path = 'state_dict.py'
    c = 0
    for k,v in state_dict.items():
        state_dict[k]['name'] = state_names[c]
        c+=1
    print(state_dict)

    with open(file_path,'w') as file:
        file.write(str(state_dict))
# update_state_info(state_names, full_state_dictionary)

# adding state bird to dictionary
def update_bird_info(bird_names, state_dict):
    file_path = 'state_dict.py'
    c = 0
    for k,v in state_dict.items():
        state_dict[k]['bird'] = bird_names[c]
        c+=1
    print(state_dict)

    with open(file_path,'w') as file:
        file.write(str(state_dict))
# update_bird_info(state_bird_list, full_state_dictionary)


# adding state capital
def add_capital(state_dict, state_capitals):
    file_path = 'state_dict.py'
    c = 0
    for k,v in state_dict.items():
        state_dict[k]['capital'] = state_capitals[c]
        c += 1

    with open(file_path, 'w') as file:
        file.write(str(state_dict))
# add_capital(full_state_dictionary, state_capitals)

def add_state_flower(state_dict, state_flowers):
    file_path = 'state_dict.py'
    c = 0
    for k,v in state_dict.items():
        state_dict[k]['flower'] = state_flowers[c]
        c += 1

    print(state_dict['AL'])
    with open(file_path,'a') as file:
        file.write(str(state_dict))

# add_state_flower(full_state_dictionary, state_flowers)

def add_gov_party(full_state_dictionary, state_govs, state_gov_party, state_land_area, state_population):
    file_path = 'state_dict.py'
    c = 0
    for k,v in full_state_dictionary.items():
        full_state_dictionary[k]['governor'] = state_govs[c]
        full_state_dictionary[k]['gov_party'] = state_gov_party[c]
        full_state_dictionary[k]['land_area'] = state_land_area[c]
        full_state_dictionary[k]['population'] = state_population[c]

        c += 1

    with open(file_path,'a') as file:
        file.write(str(full_state_dictionary))

#add_gov_party(full_state_dictionary, state_govs, state_gov_party, state_land_area, state_population)


