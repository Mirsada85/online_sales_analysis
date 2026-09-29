from product import Product
from product_manager import ProductManager

manager = ProductManager()

# Dodavanje proizvoljnih proizvoda
p1 = Product("Laptop", 1500, 5)
p2 = Product("Miš", 20, 15)
p3 = Product("Tastatura", 75, 10)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# Prikaz proizvoda i ukupne vrijednosti
manager.display_all_products()
manager.total_inventory_value()