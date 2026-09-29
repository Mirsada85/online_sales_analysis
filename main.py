from product import Product
from product_manager import ProductManager

manager = ProductManager()

# Dodavanje proizvoljnih proizvoda
p1 = Product("Super Laptop", 1600, 3)
p2 = Product("Bežični Miš", 30, 20)
p3 = Product("Mehanička Tastatura", 100, 5)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# Obrisani prikazi proizvoda i ukupne vrijednosti inventara