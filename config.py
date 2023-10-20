import os
from dotenv import load_dotenv

load_dotenv()

bird_api = os.environ.get('EBIRD_API')
open_states_api = os.environ.get('OPEN_STATE_API')
