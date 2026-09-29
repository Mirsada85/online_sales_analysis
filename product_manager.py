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
    
    def remove_product_by_name(self, name: str):
        initial_count = len(self.products)
        self.products = [p for p in self.products if p.name != name]
        if len(self.products) < initial_count:
            print(f"Proizvod '{name}' je uspješno uklonjen.")
        else:
            print(f"Proizvod '{name}' nije pronađen.")