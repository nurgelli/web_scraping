import json


def save_json(results):
    # keys = results[0].items()
    with open('product_info.json', 'w') as file:
        json.dump(results, file)
