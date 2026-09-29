# Online Sales Analysis

Ovaj projekat predstavlja sistem za analizu prodajnih podataka i upravljanje korpom u online prodavnici.

## Struktura i Klase
- **Product (`product.py`)**: Sadrži atribute `name`, `price`, `quantity`, kao i metode za prikaz i ažuriranje količine.
- **ProductManager (`product_manager.py`)**: Upravlja listom svih dostupnih proizvoda (dodavanje, prikaz, uklanjanje, ukupna vrijednost).
- **Cart (`cart.py`)**: Upravlja korpom kupca (dodavanje proizvoda, prikaz sadržaja i obračun ukupnog iznosa).
- **Main (`main.py`)**: Glavni skript za demonstraciju rada sistema.