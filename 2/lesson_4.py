# class User:
#     def __str__(self):
#         return f"User: {self.name}"

# user = User("Alice")
# print(user)

# class calculator:
#     @staticmethod
#     def add(a, b):
#         return a + b

# print(calculator.add(5, 3))

# class User:
#     count = 0
#     @classmethod
#     def show_count(cls):
#         print(f"Всего пользователей: {cls.count}")

# User.count = 5
# User.show_count()  # Выведет: Всего пользователей: 5

# class A:
#     def show_a(self):
#         print("Method from class A")

# class B(A):
#     def show_b(self):
#         print("Method from class B")

# class C(B):
#     def show_c(self):
#         print("Method from class C")

# class D(B, C):
#     def show_d(self):
#         pass

# obj = D()
# obj.show_d()

class Employee:
    company = "IT Company"
    employees_count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employees_count += 1

    def __str__(self):
        return f"Сотрудник: {self.name}, зарплата: {self.salary}"

    @classmethod
    def show_company(cls):
        print(f"Компания: {cls.company}")
        print(f"Количество сотрудников: {cls.employees_count}")

    @staticmethod
    def is_valid_salary(salary):
        return salary > 0

class Developer:
        def write_code(self):
            print("Разработчик пишет код")

class Manager:
        def manage(self):
            print("Менеджер управляет командой")

class TeamLead(Employee, Developer, Manager):
    def lead(self):
        print("Team Lead руководит командой.")

Team_lead = TeamLead("Алина", 60000)
print(Team_lead)

Employee.show_company()
print(Employee.is_valid_salary(Team_lead.salary))

Team_lead.write_code()
Team_lead.manage()
Team_lead.lead()