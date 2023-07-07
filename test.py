import ast
from abb import states

def append_to_list(file_path, new_items):
    state_names = []
    for item in new_items:
        state_names.append(item[0:-4])
    print(state_names)

    with open(file_path, 'a') as file:
        file.write(str(state_names)) 

# Usage example
file_path = 'abb.py'
append_to_list(file_path, states)


def update_dict(file_path, new_items, state_dict):
    with open(file_path, 'a') as file:
        file.write("{'al':'alabama'}")
    


dict_file_path = 'state_dict.py'
adding_dict = {'al':'alabama'}

# update_dict(dict_file_path, adding_dict, state_dict)



# def append_to_list(file_path, new_items, updating_list):

#     for item in new_items:
#         updating_list.append(item[-2:])


#     with open(file_path, 'a') as file:
#         file.write(str(updating_list)) 

# # Usage example
# file_path = 'abb.py'
# append_to_list(file_path, states, abbs)





# update_dict(state_dict, states, state_dict, abbs)
    #     data = ast.literal_eval("['al','ak']")
    #     print('data',data)
    
    # if isinstance(content, list):
    #     # Append new items to the list
    #     content.extend(new_items)
        
    #     # Save the updated list back to the file
    #     with open(file_path, 'w') as file:
    #         file.write(str(content))
    # else:
    #     print(f"File '{file_path}' does not contain a list.")
