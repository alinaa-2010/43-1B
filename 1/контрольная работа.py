#Арифметика + логика
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a > b:
    print("Первое число больше")
elif b > a:
    print("Второе число больше")
else:
    print("Числа равны")

if a > 0 and b > 0:
    print("Оба числа положительные")

#Проверка диапазона
num = int(input("Введите число: "))

if 1 <= num <= 10:
    print("Число в диапазоне 1–10")
elif 11 <= num <= 100:
    print("Число в диапазоне 11–100")
else:
    print("Число вне диапазона")

#Работа со строками
name = input("Введите имя: ")
print("Длина имени:", len(name))

if len(name) < 5:
    print("Короткое имя")
elif len(name) < 9:
    print("Среднее имя")
else:
    print("Длинное имя")

#Списки (без циклов)
numbers = [7, 3, 15, 2]
print(numbers[1])
print(numbers[3])
numbers[0], numbers[3] = numbers[3], numbers[0]
print(numbers)

#Мини-проект (Логика)
# Пользователь вводит сумму покупки
summa = float(input("Введите сумму покупки: "))

if summa > 5000:
    skidka = 0.10
elif summa > 2000:
    skidka = 0.05
else:
    skidka = 0.0  

itog = summa * (1 - skidka)

print("Размер скидки:", int(skidka*100), "%")
print("Итоговая сумма после скидки:", itog)
