from requests_html import HTMLSession
import get_csv
import get_json


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

def main():
    results = []
    for y in range(1, 5):
        print(f'Page Number {y}')
        product_links = get_links(y)
        for product in product_links:
            results.append(parse_product_links(product))
        print(f'In Total {len(results)}')
    get_csv.save_csv(results)
    get_json.save_json(results)

if __name__ == '__main__':
    main()
