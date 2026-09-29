import random
from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

# Dodavanje proizvoljnih proizvoda
p1 = Product("Super Laptop", 1600, 3)
p2 = Product("Bežični Miš", 30, 20)
p3 = Product("Mehanička Tastatura", 100, 5)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

cart = Cart()

# Odabir 3 slučajna proizvoda iz liste dostupnih proizvoda
selected_products = random.sample(manager.products, 2)
for p in selected_products:
    cart.add_to_cart(p)

# Prikaz sadržaja i ukupne vrijednosti korpe
cart.display_cart()
