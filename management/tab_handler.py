from menu import products
from .product_handler import get_product_by_id


def calculate_tab(table_bill):
    total_bill = 0

    for product in table_bill:
        item = get_product_by_id(product['_id'])
        total_bill += item["price"] * product["amount"]

    total_return = {"subtotal": f'${round(total_bill, 2)}'}

    return total_return
