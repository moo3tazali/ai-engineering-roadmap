class Product:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity

    def get_summary(self):
        # 3 x Laptop Stand = 2552.25 EGP
        return f"{self.quantity} x {self.name} = {self.get_total():.2f} EGP"


product_1 = Product("Laptop Stand", 850.75, 3)
product_2 = Product("Keyboard", 1200, 2)

print(product_1.get_summary())
print(product_2.get_summary())
