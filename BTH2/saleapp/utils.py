import json, os
from itertools import product

from saleapp import app

def read_json(path):
    with open(path, "r") as f:
        return json.load(f)

def load_categories():
    return read_json(os.path.join(app.root_path, 'data/categories.json'))

# def load_products():
#     return read_json(os.path.join(app.root_path, 'data/products.json'))

def load_products(cate_id=None, kw=None, from_price=None, to_price=None):
    products = read_json(os.path.join(app.root_path, 'data/products.json'))
    if cate_id:
        products = [p for p in products if p['category_id']==int(cate_id)]
    if kw:
        products = [p for p in products if p['name'].lower().find(kw.lower())>=0]
    if from_price:
        products = [p for p in products if p['price']>=float(from_price)]
    if to_price:
        products = [p for p in products if p['price']<=float(to_price)]
    return products

def get_product_by_id(product_id):
    products = read_json(os.path.join(app.root_path, 'data/products.json'))

    for p in products:
        if p['id']==product_id:
            return p

# def add_employees(data, ma, name, description, price, image, category_id):
#     em = {
#         "id": ma,
#         "name": name,
#         "description": description,
#         "price": price,
#         "image": image,
#         "category_id": category_id
#     }
#     data.append(em)
#     with open("data/products.json", mode="w",encoding='utf-8') as f:
#         json.dump(data,f,ensure_ascii=False, indent=4)

# def load_products():
#     with open('data/products.json', 'r') as f:
#         return json.load(f)

def get_next_product_id():
    products = load_products()
    if products:
        return max(product['id'] for product in products) + 1
    return 1