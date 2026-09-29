from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)
        print(f"Dodat proizvod: {product.name}")

    def display_all_products(self):
        print("\n--- Lista svih proizvoda ---")
        for product in self.products:
            product.display_info()

    def total_inventory_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        print(f"\nUkupna vrijednost inventara: {total} KM")
        return total
    