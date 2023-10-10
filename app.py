from flask import Flask, Blueprint, render_template
from state_dict_folder.state_dict import full_state_dictionary

app = Flask(__name__)
app.debug = True

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', full_state_dictionary = full_state_dictionary)


@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/map2')
def map2():
    return render_template('map2.html')


@app.route('/gpt')
def gpt():
    return render_template('gpt.html')


@app.route('/search')
def route():
    return render_template('search.html', full_state_dictionary=full_state_dictionary)

if __name__ == '__main__':
    app.run(debug=True)