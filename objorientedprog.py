class Car:

    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def show_info(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Speed :", self.speed, "km/h")

    def accelerate(self, amount):
        self.speed += amount
        print("New speed:", self.speed, "km/h")

    def brake(self, amount):
        self.speed -= amount

        if self.speed < 0:
            self.speed = 0

        print("New speed:", self.speed, "km/h")


car1 = Car("BMW", "M4", 120)

car1.show_info()

print("\nAccelerating...")
car1.accelerate(50)

print("\nBraking...")
car1.brake(30)
