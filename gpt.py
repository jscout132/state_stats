
from state_dict import full_state_dictionary
from main import abbs
from states import state_bird_list, state_capitals


def add_abbs(abbs, full_state_dictionary, new_info):
    file_path = 'state_dict.py'
    for abb in abbs:
        full_state_dictionary.update({abb:new_info})
    with open(file_path,'w') as file:
        file.write(str(full_state_dictionary))

new_info = {
    'bird':'holder',
    'capital':'holder',
    'flower':'holder',
    'governor':'holder',
    'land_area':'holder',
    'name':'holder',
    'population':'holder',
}
# add_abbs(abbs, full_state_dictionary, new_info)


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

    print(state_dict['AL'])

    with open(file_path, 'w') as file:
        file.write(str(state_dict))


add_capital(full_state_dictionary, state_capitals)

    # Search for the line containing the state you want to update
    # state_line_index = None
    # for i, line in enumerate(lines):
    #     if state_name in line:
    #         state_line_index = i
    #         break

    
    # if state_line_index is not None:
    #     # Update the line with the new information
    #     updated_line = f"{state_name} = {new_info}"
    #     lines[state_line_index] = updated_line
    
    #     # Write the updated content to a temporary file
    #     with open(temp_file_path, 'w') as temp_file:
    #         temp_file.writelines(lines)
        
    #     # Replace the original file with the updated file
    #     shutil.move(temp_file_path, file_path)
    # else:
    #     print(f"State '{state_name}' not found in the file.")

# Usage example

# def update_dictionary(file_path, key, new_value):
#     with open(file_path, 'r') as file:
#         content = file.read()
#         data = content
#         print(data)
    
#     # Update the value of the specified key
#     for i in dict(data):
#         print(i)
#     data[key] = new_value
    
#     # Save the updated dictionary back to the file
#     with open(file_path, 'w') as file:
#         file.write(str(data))


# # Usage example
# file_path = 'abb.py'
# key = 'al'
# new_value = 'Montgomery'
# update_dictionary(file_path, key, new_value)
