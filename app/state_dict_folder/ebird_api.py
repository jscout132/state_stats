import os
import requests
import sys

sys.path.append("../state_stats")
from config import bird_api

from state_dict import full_state_dictionary

bird_dict = {}
class BirdDictionary:
    def __init__(self, bird_names, scientific_names, species_codes):
        self.bird_names = bird_names
        self.scientific_names = scientific_names
        self.species_codes = species_codes

    def bird_flow(self):
        bird.find_com_name()
        bird.create_name_dict()
        bird.find_bird_info()
        bird.create_bird_dict()

    def find_com_name(self):
        main_url = "https://api.ebird.org/v2/ref/taxonomy/ebird?fmt=json"
        full_response = requests.request("GET", main_url).json()
        for v in full_state_dictionary.values():
            for response in full_response:
                if v["bird"] == response["comName"]:
                    self.scientific_names.append(response["sciName"])
                    self.species_codes.append(response["speciesCode"])
        return self.scientific_names, self.species_codes
    
    def create_name_dict(self):
        c = 0
        for k,v in full_state_dictionary.items():
            bird_dict.update({k:{'bird':v['bird'], 'scientific_name':self.scientific_names[c], 'species_code':self.species_codes[c], 'bird_count':0, 'loc_count':0, 'loc_dict':{}}})
            c+=1

    def find_bird_info(self):
        payload = {}
        headers = {"X-eBirdApiToken": bird_api}
        for k,v in bird_dict.items():
            species_url = f"https://api.ebird.org/v2/data/obs/US-{k}/recent/{v['species_code']}/?back=1"
            responses = requests.request("GET", species_url, headers=headers, data=payload).json()
            for response in responses:
                if responses == []:
                    pass
                elif response['locId'] in v['loc_dict']:
                    pass
                elif 'howMany' in response:
                    v['loc_dict'].update({response['locId']:{'lat':response['lat'],'lon':response['lng']}},)   
                    v['bird_count'] += response['howMany']
                else:
                    v['loc_dict'].update({response['locId']:{'lat':response['lat'],'lon':response['lng']}},)   
                    v['bird_count'] += 0
            v['loc_count'] = len(v['loc_dict']) 
        return bird_dict
            
    def create_bird_dict(self):
        with open('app/state_dict_folder/ebird_dict.py','w') as file:
            file.write(f'bird_dict={bird_dict}')
        

bird = BirdDictionary([], [], [])
bird.bird_flow()
