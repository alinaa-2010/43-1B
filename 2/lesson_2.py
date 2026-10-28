

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def info(self):
#         return f"Name: {self.name}, Email: {self.email}"

# class Employee(User):
#     def __init__(self, name, email, position):
#         super().__init__(name, email)
#         self.position = position

#     def info(self):
#         return f"Name: {self.name}, Email: {self.email}, Position: {self.position}"

# emp = Employee("Alice", "alice@gmail.com", "Software Engineer")
# print(emp.info())

# """
# создать класс waiter для официанта, который наследуется 
# от класса Employee и имеет дополнительный атрибут "restaurant"
#  (название ресторана). Переопределить метод info() для отображения
#   информации о официанте вместе с названием ресторана."""


# class Pay:
#     def info(self):
#         return "Метод Оплаты"
# 
# class CardPayment(Pay):
#     def info(self):
#         return "Оплата картой"
# 
# class CashPayment(Pay):
#     def info(self):
#         return "Оплата наличными"
# 
# payments = [
#     Pay(),
#     CardPayment(),
#     CashPayment()
# ]
# 
# for payment in payments:
#     print(payment.info())

class Animal:
    
    def info(self):
        return "Какие зыуки издауют животные"
    
class Cats(Animal):
    def info(self):
        return "Мяууу"
class Dogs(Animal):
    def info(self):
        return "Гав гав"
    
class cows(Animal):
    def info(self):
        return "Муууу"
        
animals = [
    Cats(),
    Dogs(),
    cows()
]

for sound in animals:
    print(sound.info())