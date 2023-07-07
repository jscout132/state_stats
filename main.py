import requests
from bs4 import BeautifulSoup
# from states import states

url = 'https://www.50states.com/alabama.htm'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="content")


bird_url = "https://www.50states.com/bird/"
birds = requests.get(bird_url)
soup = BeautifulSoup(birds.content,"html.parser")
results = soup.find(id="post-748")
bird_list = results.find_all("div", class_="row")
state_bird_list = []
for bird in bird_list:
    state = bird.find('div', class_="col-sm-5 flagsCols textCenter")
    if state == None:
        continue
    else:
        state_bird_list.append(state.text)
print(state_bird_list)
# quick_facts = results.find_all("ul")
# print(type(quick_facts))
# c = 0
# for quick_fact in quick_facts:
#     capital_city = quick_fact.find("li").text
#     c = c+ 1
# print(capital_city)
# print(c)

import shutil
import ast
# for i in states:
#     print(i[-2:])

def update_state_abb(var_name):
    file_path = 'abb.py'
    temp_file_path = 'holder_abb.py'

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i in range(0,len(lines)):
        updated_abb = f"{lines[i].strip()[-4:-2]}"
        
        with open(temp_file_path, 'w') as temp_file:
            temp_file.writelines(var_name.append(updated_abb))

        shutil.move(temp_file_path, file_path)
    # state_line_index = None
    # for i, line in enumerate(lines):


    # if state_line_index is not None:
    #     updated_line = f"{var_name}= '{new_info}'"
    #     lines[state_line_index] = updated_line

    #     with open(temp_file_path, 'w') as temp_file:
    #         temp_file.writelines(lines)
        
    #     shutil.move(temp_file_path, file_path)
    # else:
    #     print(f"{var_name} not found in the file")


updated_info = {}
var_name = 'abbs'
# update_state_abb(var_name)

abbs=['AK', 'AL', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
states = [
    'Alaska: AK', 
    'Alabama: AL',
    'Arizona: AZ',
    'Arkansas: AR',
    'California: CA',
    'Colorado: CO',
    'Connecticut: CT',
    'Delaware: DE',
    'Florida: FL',
    'Georgia: GA',
    'Hawaii: HI',
    'Idaho: ID',
    'Illinois: IL',
    'Indiana: IN',
    'Iowa: IA',
    'Kansas: KS',
    'Kentucky: KY',
    'Louisiana: LA',
    'Maine: ME',
    'Maryland: MD',
    'Massachusetts: MA',
    'Michigan: MI',
    'Minnesota: MN',
    'Mississippi: MS',
    'Missouri: MO',
    'Montana: MT',
    'Nebraska: NE',
    'Nevada: NV',
    'New Hampshire: NH',
    'New Jersey: NJ',
    'New Mexico: NM',
    'New York: NY',
    'North Carolina: NC',
    'North Dakota: ND',
    'Ohio: OH',
    'Oklahoma: OK',
    'Oregon: OR',
    'Pennsylvania: PA',
    'Rhode Island: RI',
    'South Carolina: SC',
    'South Dakota: SD',
    'Tennessee: TN',
    'Texas: TX',
    'Utah: UT',
    'Vermont: VT',
    'Virginia: VA',
    'Washington: WA',
    'West Virginia: WV',
    'Wisconsin: WI',
    'Wyoming: WY']
