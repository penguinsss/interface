import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def build_data():
    with open(BASE_DIR + '/login.json', encoding='utf-8') as f:
        data = json.load(f)
        data_list = []
        for i in data:
            data_list.append((i.get('username'),
                              i.get('password'),
                              i.get('verify_code'),
                              i.get('expect'),
                              i.get('status')))
        return data_list
