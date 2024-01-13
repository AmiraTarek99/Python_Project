import json
def load_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    return data

def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)