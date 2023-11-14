class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(f"Book Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity Available: {self.quantity}")


book1 = Book('The Financier', 10.99, 50, 'T. Dreiser')
book2 = Book('Flowers for Algernon', 15.00, 10, 'D. Keyes')

book1.read()
