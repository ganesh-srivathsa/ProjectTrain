# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


# Child class
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def show_details(self):
        self.display()
        print("Fuel Type:", self.fuel_type)


# Creating an object
car1 = Car("Toyota", "Innova", "Diesel")

# Calling methods
car1.show_details()