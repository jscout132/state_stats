from state_dict import full_state_dictionary

api_key = '3a216c9d-506b-470f-9268-6b5dcd40df1e'

# using /people.geo search
def find_senators():
    for k,v in full_state_dictionary.items():
        open_states_url = f'https://v3.openstates.org/people.geo?lat={v["lat"]}&lng={v["lon"]}&apikey={api_key}'
