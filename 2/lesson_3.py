# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount

#     def get_balance(self):
#         return self.__balance

# account = BankAccount(1000)

# print(account.get_balance())

# class Computer:

#     def __init__(self, brand, volume, password):
#         self.__brand = brand
#         self.__volume = volume
#         self.__password = password

#     # Getter for volume
#     @property
#     def volume(self):
#         return self.__volume

#     # Setter for volume
#     @volume.setter
#     def volume(self, value):
#         if 0 <= value <= 100:
#             self.__volume = value
#         else:
#             print("Volume must be between 0 and 100.")

#     # Getter for password
#     @property
#     def password(self):
#         return self.__password

#     # Setter for password
#     @password.setter
#     def password(self, value):
#         if len(value) >= 8:
#             self.__password = value
#         else:
#             print("Password must be at least 8 characters long.")


# pc = Computer("Dell", 50, "securepass")

# from abc import ABC, abstractmethod

# class Car(ABC):

#     @abstractmethod
#     def start_engine(self):
#         pass

# class BMW(Car):
#     def start_engine(self):
#         return "BMW engine started"

# class Toyota(Car):
#     def start_engine(self):
#         return "Toyota engine started"

# bmw = BMW()
# toyota = Toyota()

# print(bmw.start_engine())  
# print(toyota.start_engine())

from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def move(self):
        pass


class Car(Transport):

    def __init__(self, speed):
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            self.__speed = 0
        elif value > 300:
            self.__speed = 300
        else:
            self.__speed = value

    def move(self):
        print(f"car moves at {self.speed} км/ч")


class Bike(Transport):

    def move(self):
        print("Bike moved")


class Bus(Transport):

    def move(self):
        print("Bus moved")


def main():
    car = Car(100)
    bike = Bike()
    bus = Bus()

    car.move()
    bike.move()
    bus.move()


main()