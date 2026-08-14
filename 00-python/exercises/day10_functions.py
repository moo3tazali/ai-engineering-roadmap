products = [
    {"name": "Laptop Stand", "price": 850.75, "quantity": 3},
    {"name": "Keyboard", "price": 1200, "quantity": 2},
]


def calculate_total(price, quantity):
    return price * quantity


def get_product_summary(product):
    # 3 x Laptop Stand = 2552.25 EGP
    return f"{product['quantity']} x {product['name']} = {calculate_total(product['price'], product['quantity']):.2f} EGP"


for product in products:
    print(get_product_summary(product))


def get_user():
    return "Moataz", "Egypt"


name, country = get_user()
print(f"{name} - {country}")
