# tuple_1 = (1,2,3)
# print(id(tuple_1))
# tuple_2 = (4,5,6)
# print(id(tuple_2))
# main_tuple = tuple_1 + tuple_2
# print(id(main_tuple))
# print(main_tuple)
# 
# new_tuple = main_tuple
# print(id(new_tuple))
# 
# def hello():
#     print("Hello World")
# 
# print(id(hello))
# 
# 
# 
# 
# 
# 
# 
# class User:
#     pass
# 
# user1 = User()
# user2 = User()
# 
# 


# class Car:
#     def __init__(self, model, created_at):
#         self.model = model
#         self.created_at = created_at
# 
# car1 = Car("BMW", 2020)
# car2 = Car("Audi", 2021)
# print(car1)
# print(car2)
# print(car1.model)
# print(car1.created_at)


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"Name: {self.name}, Age: {self.age}"

dog = Animal("Bob", 5)
# print(dog.name)
# print(dog.age)
print(dog.info())
"""
ТЗ: BankAccount

Создать класс BankAccount с атрибутами:

owner — владелец счёта;
balance — баланс.

Добавить методы:

deposit(amount) — пополнение счёта;
withdraw(amount) — снятие денег.
Проверка
Создать счёт Beksultan с балансом 1000.
Пополнить на 500.
Снять 200.
Вывести итоговый баланс.

Ожидаемый результат: 1300.

Дополнительно: не разрешать снять сумму больше текущего баланса."""