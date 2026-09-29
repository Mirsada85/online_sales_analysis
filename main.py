import random
from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

p1 = Product("Laptop", 1500, 5)
p2 = Product("Miš", 20, 15)
p3 = Product("Tastatura", 75, 10)
p4 = Product("Slušalice", 50, 8)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)
manager.add_product(p4)

# Rad sa korpom
cart = Cart()

# Odabir 3 slučajna proizvoda iz liste dostupnih proizvoda
selected_products = random.sample(manager.products, 3)
for p in selected_products:
    cart.add_to_cart(p)

# Prikaz sadržaja i ukupne vrijednosti korpe
cart.display_cart()