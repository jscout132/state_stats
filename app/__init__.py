from flask import Flask
from flask_cors import CORS
from flask_session import Session

# from .state_dict_folder.state_dict import full_state_dictionary
from .site.routes import site

app = Flask(__name__)
CORS(app)

Session(app)

app.register_blueprint(site)

# @app.route('/map')
# def map():
#     return render_template('map.html')

# @app.route('/map2')
# def map2():
#     return render_template('map2.html')


# @app.route('/gpt')
# def gpt():
#     return render_template('gpt.html')


# @app.route('/search')
# def route():
#     return render_template('search.html', full_state_dictionary=full_state_dictionary)

if __name__ == '__main__':
    app.run(debug=True)