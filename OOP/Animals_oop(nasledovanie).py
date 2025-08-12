from abc import ABC, abstractmethod

import logging

# Базовая настройка логов: уровень и формат
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

class LogMixin:
    @property
    def logger(self):
        # имя логгера — имя класса (удобно в больших проектах)
        return logging.getLogger(self.__class__.__name__)

    def log_info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def log_warn(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def log_error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    def describe(self):
        return f"{type(self).__name__} named {self.name}"
    @abstractmethod
    def speak(self):
        pass
    
class Dog(LogMixin, Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        self.log_info("Dog created: name=%s, Breed=%s", self.name, self.breed)
    def speak(self):
        self.log_info("Dog.speak called for %s", self.name)
        return f"{self.name}, {self.breed} barks"
    
class Cat(LogMixin, Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        self.log_info("Cat created: name=%s, Breed=%s", self.name, self.breed)
    def speak(self):
        self.log_warn("Cat.speak called for %s", self.name)
        return f"{self.name}, {self.breed} meows"
        
animals = [
    Dog("Zhulia", "Chivinny"),
    Cat("Murka", "Russian Blue")
]

for a in animals:
    print(a.describe())
    print(a.speak())
