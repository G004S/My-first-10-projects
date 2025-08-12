from datetime import datetime
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

#PARENT CLASS
class Animal(ABC):
    _id_seq = 0
    def __init__(self, name, age):
        Animal._id_seq += 1
        self.__id = Animal._id_seq
        self._name = name
        self._age = None
        self.age = age
        self._created_at = datetime.now()
    @property
    def name(self):
        return self._name
    @property
    def id(self):
        return self.__id
    @property
    def age(self):
        return self._age
    @property
    def created_at(self):
        return self._created_at
    @property
    def is_adult(self):
        return self._age >= 1
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("Age must be an integer")
        if value < 0:
            raise ValueError("Age must be a non-zero number")
        self._age = value
    def describe(self):
        return f"{type(self).__name__} named {self.name}"
    @abstractmethod
    def speak(self):
        pass
#DOGS
class Dog(LogMixin, Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self._breed = breed
        self.log_info("Dog created: name=%s, Breed=%s", self.name, self.breed)
    def speak(self):
        self.log_info("Dog.speak called for %s", self.name)
        return f"{self.name}, {self.breed}, {self.age}, barks"
    @property
    def breed(self):
        return self._breed

#CATS
class Cat(LogMixin, Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self._breed = breed
        self.log_info("Cat created: name=%s, Breed=%s", self.name, self.breed)
    @property
    def breed(self):
        return self._breed
    def speak(self):
        self.log_warn("Cat.speak called for %s", self.name)
        return f"{self.name}, {self.breed}, {self.age}, meows"
        

a0 = Dog("Zhulia", 12, "Chivinny")
a1 = Cat("Murka", 17, "Russian Blue")

print(a0.name, a0.breed, a0.created_at, a0.is_adult, a0._Animal__id)
print(a1.name, a1.breed, a1.created_at, a1.is_adult, a1._Animal__id)