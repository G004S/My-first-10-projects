from functools import total_ordering
@total_ordering
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
    
    def __eq__(self, other):
        if not isinstance (other, Car):
            return NotImplemented
        return (self.make, self.model, self.year) == (other.make, other.model, other.year)
    def __lt__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return (self.year, self.make, self.model) < (other.year, other.make, other.model)


cars = [
    Car("Toyota", "Corolla", 2020),
    Car("Honda", "Civic", 2019),
    Car("Ford", "Mustang", 2021),
    Car("Ford", "Kucha", 2022),
    Car("VW", "GOLF", 2002)
]

for car in sorted(cars, reverse=True):
    print(car)
