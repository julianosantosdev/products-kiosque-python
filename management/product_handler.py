from menu import products


def get_product_by_id(prod_id):
    if type(prod_id) != int:
        raise TypeError("product id must be an int")

    for product in products:
        if product["_id"] == prod_id:
            return product

    else:
        return {}


def get_products_by_type(prod_type):
    if type(prod_type) != str:
        raise TypeError("product type must be a str")

    found_products = []
    for product in products:
        if product["type"] == prod_type:
            found_products.append(product)

    else:
        return found_products


def add_product(menu, **product_to_add):
    id_list = []
    new_id = 0
    new_product = {}

    if len(menu) == 0:
        new_id = 1
        new_product["_id"] = new_id
    else:
        for product in menu:
            id_list.append(product["_id"])
        id_list.sort()
        new_product["_id"] = id_list[-1] + 1

    keys = list(product_to_add.keys())
    values = list(product_to_add.values())

    for index, key in enumerate(keys):
        new_product[keys[index]] = values[index]

    menu.append(new_product)
    print(new_product)
    return new_product


def menu_report():
    product_quantity = len(products)
    product_average_price = 0
    product_most_common_list = []
    product_types = []
    product_type_count = {}
    most_common_product = ""

    for product in products:
        product_average_price += product['price']
        product_most_common_list.append(product["type"])
        if not product_types.__contains__(product['type']):
            product_types.append(product['type'])

    for type in product_types:
        product_type_count[type] = product_most_common_list.count(type)

    for keys, values in product_type_count.items():
        if values == max(product_type_count.values()):
            most_common_product = keys

    return_msg = f'Products Count: {product_quantity} - Average Price: ${round((product_average_price/product_quantity), 2)} - Most Common Type: {most_common_product}'
    return return_msg
