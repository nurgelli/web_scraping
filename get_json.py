import json


def save_json(results):

    with open('product_info.json', 'w') as file:
        json.dump(results, file)
