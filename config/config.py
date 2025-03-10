import os
import json

CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(CONFIG_DIR, 'config.json')

with open(config_path, 'r') as file:
    json_config = json.load(file)

SPREADSHEET_ID = json_config.get('SPREADSHEET_ID')
RANGE_NAME = json_config.get('RANGE_NAME')
CATEGORIES = json_config.get('CATEGORIES')