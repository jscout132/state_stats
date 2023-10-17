from flask import Blueprint, render_template, redirect

from ..state_dict_folder.state_dict import full_state_dictionary, sorted_pop, sorted_land_area

site = Blueprint('site',__name__, template_folder='site_pages')

@site.route('/')
@site.route('/home')
def home():
    return render_template('index.html', full_state_dictionary = full_state_dictionary)


@site.route('/state/<state_code>')
def state(state_code):
    state_data = full_state_dictionary.get(state_code)
    if state_data:
        return render_template('state.html', full_state_dictionary=full_state_dictionary, state_data=state_data, sorted_pop=sorted_pop, sorted_land_area=sorted_land_area)
    else:
        return "State not found", 404
            

