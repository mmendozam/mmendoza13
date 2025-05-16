import os
import json

BASE_PATH = 'G:/ZWOLF_HOME/_Nanalka/media/videos/tokyomotion'

for filename in os.listdir(BASE_PATH):
    if filename.endswith('.json'):
        with open(f'{BASE_PATH}\{filename}', 'r', encoding='utf-8') as my_file:
            content = my_file.read()
            my_json = json.loads(content)
            print(f'{my_json.get("webpage_url")}')
