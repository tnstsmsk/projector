class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed = max(0, self.speed - 5)

    def display_speed(self):
        return self.speed


my_car = Car('Porsche', '911', 2021)


my_car.accelerate()
print(f"Current speed: {my_car.display_speed()} mph")

my_car.accelerate()
print(f"Current speed: {my_car.display_speed()} mph")

my_car.brake()
print(f"Current speed: {my_car.display_speed()} mph")

my_car.brake()
print(f"Current speed: {my_car.display_speed()} mph")

my_car.brake()
print(f"Current speed: {my_car.display_speed()} mph")
