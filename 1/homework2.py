#Задача 1
a = float(input("введите число: "))
b = float(input("введите второе число: "))
znak = input("введите знак (+, -, *, /): ")

if znak == "+":
    print("Результат:", a + b)
elif znak == "-":
    print("Результат:", a - b)
elif znak == "*":
    print("Результат:", a * b)
elif znak == "/":
    if b == 0:
        print("Ошибка: деление на ноль")
    else:
        print("Результат:", a / b)

#Задача 2
login = "admin"
password = "1234"

user_login = input("Введите логин: ")
user_password = input("Введите пароль: ")

if user_login == login and user_password == password:
    print("Доступ разрешен")
else:
    print("Ошибка")

#Задача 3
score = int(input("Введите балл (0-100): "))

if 90 <= score <= 100:
    print("Отлично")
elif 70 <= score <= 89:
    print("Хорошо")
elif 50 <= score <= 69:
    print("Удовлетворительно")
else:
    print("Не сдал")

#Задача 4
day = int(input("Введите число от 1 до 7: "))

if day == 1:
    print("Понедельник")
elif day == 2:
    print("Вторник")
elif day == 3:
    print("Среда")
elif day == 4:
    print("Четверг")
elif day == 5:
    print("Пятница")
elif day == 6:
    print("Суббота")
elif day == 7:
    print("Воскресенье")
else:
    print("Ошибка: число должно быть от 1 до 7")