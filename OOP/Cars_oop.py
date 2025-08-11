class Car:
    wheels = 4 
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def __str__ (self):
        return f"{self.year} {self.make} {self.model}, (wheels: {Car.wheels}) "
    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}', year={self.year})"

cars = [
    Car("Toyota", "Corolla", 2020),
    Car("Honda", "Civic", 2019),
    Car("Ford", "Mustang", 2021),
    Car("Chevrolet", "Camaro", 2022)
]
for car in cars:
    print(car)