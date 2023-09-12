# pylint:disable-all

class Inventory:
    def __init__(self, max_products):
        self.products = {}
        self.max_products = max_products

    def size(self):
        return len(self.products)

    def add_product(self, product_name, stock_quantity):
        if len(self.products) == self.max_products:
            raise OverflowError("Inventory's limit has been reached")
        else:
            self.products[product_name] = stock_quantity

    def update_stock(self, product_name, new_stock_quantity):
        if product_name in self.products:
            self.products[product_name] = new_stock_quantity
        else:
            raise ValueError(f"Product {product_name} not found in inventory")

    def get_stock(self, product_name) -> int:
        if product_name in self.products:
            return self.products[product_name]
        else:
            raise ValueError(f"Product {product_name} not found in inventory")

    def calculate_stock_value(self, price_map):
        value = 0
        for product_name, stock_quantity in self.products.items():
            unit_price = price_map.get(product_name)
            value += unit_price * stock_quantity
        return value
