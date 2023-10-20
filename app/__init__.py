from flask import Flask
from flask_cors import CORS
from flask_session import Session

# from .state_dict_folder.state_dict import full_state_dictionary
from .site.routes import site

app = Flask(__name__)
CORS(app)

Session(app)

app.register_blueprint(site)

if __name__ == '__main__':
    app.run(debug=True)