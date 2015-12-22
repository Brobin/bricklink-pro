from models import Set, Part
from config import API_KEY
import requests
import json
import sys


PARTS_URL = 'https://rebrickable.com/api/get_set_parts'


def get_set_parts(set_id):
    params = { 'key': API_KEY, 'format': 'json', 'set': set_id }
    response = requests.get(PARTS_URL, params)
    data = json.loads(response.text)[0]
    parts = []
    for p in data['parts']:
        parts.append(Part(p['part_id'], p['element_id'], p['qty']))
    return Set(data['set_id'], data['descr'], parts)


def create_setlist(set_id):
    lego_set = get_set_parts(set_id)
    with open(lego_set.parts_file, 'w+') as csv:
        csv.write(str(lego_set))
    return lego_set


if __name__ == '__main__':
    try:
        set_id = sys.argv[1]
    except:
        set_id = '75102-1'
    create_setlist(set_id)
    
