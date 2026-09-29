import random

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)
        print(f"Dodato u korpu: {product.name}")

    def calculate_total(self):
        total = sum(product.price for product in self.cart_items)
        return total

    def display_cart(self):
        print("\n--- Sadržaj korpe ---")
        for item in self.cart_items:
            item.display_info()
        print(f"Ukupno za uplatu: {self.calculate_total()} KM")