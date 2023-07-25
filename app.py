from flask import Flask, Blueprint, render_template
from state_dict_folder.state_dict import full_state_dictionary

app = Flask(__name__)
app.debug = True

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', full_state_dictionary = full_state_dictionary)

if __name__ == '__main__':
    app.run(debug=True)