from requests_html import HTMLSession
import csv




sess = HTMLSession()

def get_links(page):
    
       
    url = sess.get(f'https://themes.woocommerce.com/storefront/category-clothing/clothing/page/{page}')
    products = url.html.find('ul.products li ')
    links = [item.find('a', first=True).attrs['href'] for item in products]  
    return links



def parse_product_links(url):

    element = sess.get(url)
    
    title = element.html.find('h1.product_title.entry-title', first=True).text.strip()
    price = element.html.find('p.price', first=True).text.strip().replace('\n', '/')
    category = element.html.find('span.posted_in', first=True).text.strip()
    try:
        sku = element.html.find('span.sku', first=True).text.strip()
    except AttributeError as err:
        sku = 'None'
    try:
        tag = element.html.find('span.tagged_as', first=True).text.strip()
    except AttributeError as err:
        tag = 'None'
    try:
        weight = element.html.find('td.woocommerce-product-attributes-item__value', first=True).text.strip()
    except AttributeError as err:
        weight = 'None'

    about_product = {
        "title": title,
        "price": price,
        "sku": sku,
        "category": category,
        "tag": tag,
        "weight": weight
    }
    return about_product

def save_csv(results):
    keys = results[0].keys()
    try:
        with open('products_info.csv', 'w', encoding='utf-8') as file:
            product_writer = csv.DictWriter(file, keys)
            product_writer.writeheader()
            product_writer.writerows(results)
    except NotImplementedError as err:
        print(f"Can't be written {err}")



results = []
for y in range(1, 5):
    print(f'Page Number {y}')
    product_links = get_links(y)
    for product in product_links:
        results.append(parse_product_links(product))
    print(f'In Total {len(results)}')
save_csv(results)

