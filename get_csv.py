import csv

def save_csv(results):
    keys = results[0].keys()
    try:
        with open('products_info.csv', 'w', encoding='utf-8') as file:
            product_writer = csv.DictWriter(file, keys)
            product_writer.writeheader()
            product_writer.writerows(results)
    except NotImplementedError as err:
        print(f"Can't be written {err}")