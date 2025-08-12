from abc import ABC, abstractmethod
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

class LogMixin:
    @property
    def logger(self):
        return logging.getLogger(self.__class__.__name__)

    def log_info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def log_warn(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def log_error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

class Animal(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = None
        self.age = age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("Age must be an integer")
        if value < 0:
            raise ValueError("Age must be a positive number")
        self._age = value
    def describe(self):
        return f"{type(self).__name__} named {self.name}"
    @abstractmethod
    def speak(self):
        pass
    
class Dog(LogMixin, Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
        self.log_info("Dog created: name=%s, Breed=%s", self.name, self.breed)
    def speak(self):
        self.log_info("Dog.speak called for %s", self.name)
        return f"{self.name}, {self.breed}, {self.age}, barks"
    
class Cat(LogMixin, Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
        self.log_info("Cat created: name=%s, Breed=%s", self.name, self.breed)
    def speak(self):
        self.log_warn("Cat.speak called for %s", self.name)
        return f"{self.name}, {self.breed}, {self.age}, meows"
        
animals = [
    Dog("Zhulia", 15, "Chivinny"),
    Cat("Murka", 17, "Russian Blue")
]

for a in animals:
    print(a.describe())
    print(a.speak())