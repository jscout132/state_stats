import sys
sys.path.append("../state_stats")

from state_dict import full_state_dictionary

from config import open_states_api

# TODO: add US senators
# using /people.geo search
def find_senators():
    for k,v in full_state_dictionary.items():
        open_states_url = f'https://v3.openstates.org/people.geo?lat={v["lat"]}&lng={v["lon"]}&apikey={open_states_api}'
