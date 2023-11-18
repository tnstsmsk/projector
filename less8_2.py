class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


class Warehouse:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product, quantity):
        self.inventory[product] = quantity

    def view_stock(self):
        return self.inventory


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = {}

    def add_to_cart(self, product, quantity):
        if product in self.shopping_cart:
            self.shopping_cart[product] += quantity
        else:
            self.shopping_cart[product] = quantity

    def view_cart(self):
        return self.shopping_cart

    def clear_cart(self):
        self.shopping_cart.clear()


class Order:
    def __init__(self, user, warehouse):
        self.user = user
        self.warehouse = warehouse

    def place_order(self):
        for product, quantity in self.user.shopping_cart.items():
            if product in self.warehouse.inventory and self.warehouse.inventory[product] >= quantity:
                self.warehouse.inventory[product] -= quantity
            else:
                print(f"Insufficient stock for {product.name}. Order not placed.")
        self.user.clear_cart()

# Create warehouse and products
warehouse = Warehouse()
apple = Product("Apple", "Fresh Red Apple", 0.5)
banana = Product("Banana", "Fresh Yellow Banana", 0.3)

# Add products to warehouse
warehouse.add_product(apple, 100)
warehouse.add_product(banana, 150)

# Create a user
user = User("John Doe", "john.doe@example.com")

# User adds items to cart
user.add_to_cart(apple, 5)
user.add_to_cart(banana, 10)

print("User's Cart:")
for product, quantity in user.view_cart().items():
    print(f"{product.name}: {quantity}")

# User places an order
order = Order(user, warehouse)
order.place_order()

# User views items in cart after order is placed (should be empty)
print("User's Cart after Placing Order:")
print(user.view_cart())  # Output: {}

# View stock after order is placed
print("Warehouse Stock:")
for product, quantity in warehouse.view_stock().items():
    print(f"{product.name}: {quantity}")
