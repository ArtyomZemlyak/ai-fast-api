import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))

from ai_fast_api.app_generator import generate_api
from api import DocAPI

doc_api = DocAPI()
app = generate_api(doc_api)
