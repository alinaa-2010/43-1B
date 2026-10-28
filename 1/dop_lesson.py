# задание 1
# name = input("Введите ваше имя: ")
# age = int(input("Введите ваш возраст: "))
# price = float(input("Введите цену одного товара: "))

# print("\nРезультат")
# print(f"Привет, {name}! Тебе {age} лет.")

# total_price = price * 3
# print(f"Цена 3 таких товаров: {total_price} сом")

# money = 1000
# ostatok = money - total_price
# print(f"Если у тебя есть {money} сом, то после покупки останется: {ostatok} сом")

# задание 2
# age = int(input("Введите ваш возраст: "))
# if age < 7:
#     print("Ты еще не ходишь в школу")
# elif age <= 17:
#     print("Ты ходишь в школу")
# elif age <= 23:
#     print("Ты студент")
# else:
#     print("Ты работаешь или учишься дальше")

# # дополнительно
# if age < 18:
#     print("Ты несовершеннолетний")
# else:
#     print("Ты совершеннолетний")

# задание 3
# fruits = ["orange","lemon", "apple","pineapple","kiwi"]
# print("Первый фрукт:", fruits[0])
# print("Последний фрукт:", fruits[4])

# print("Фрукты по отдельности:")
# for fruit in fruits:
#     print(fruit)

# print("Количество фруктов:", len(fruits))

# if "яблоко" in fruits:
#     print("Яблоко есть в списке")
# else:
#     print("Яблока нет в списке")

# задание 4 
# cities = ["Bishkek", "Osh", "Talas", "Naryn", "Issyk-Kul"]
# colors = ("black", "white", "blue")

# print("Список городов:", cities)
# print("Второй город:", cities[1])
# print("Кортеж цветов:", colors)
# print("Первый цвет:", colors[0])
# print("Последний цвет:", colors[-1])
# print("Количество городов:", len(cities))
# print("Количество цветов:", len(colors))

# задание 5
student = {
    "name": "Alina",
    "age": 15,
    "group": "39-B1"
}

words = {"apple", "banana", "kiwi", "apple", "pineapple", "car"}

print("Словарь student:", student)
print("Имя:", student["name"])
print("Группа:", student["group"])
print("Множество слов:", words)
print("Количество уникальных слов:", len(words))

# задание 6
def proizvedenye(num1,num2):
    print(num1 * num2)

result1 = proizvedenye(5, 2)
result2 = proizvedenye(6, 1)
result3 = proizvedenye(2, 3)

print(f"Результат 1: {result1}")
print(f"Результат 2: {result2}")
print(f"Результат 3: {result3}")

# задание 7
numbers = [2, 4, 6, 8, 10]
nums = list(map(lambda x: x + 5, numbers))
print(nums)

# задание 8
with open("data.txt", "w") as file:
    file.write("Alina\n")
    file.write("Nurbek\n")
    file.write("Bekbolot\n")
    file.write("Ruslan\n")

with open("data.txt", "r") as file:
    names = file.readlines()

names = [name.strip() for name in names]

print("Все имена:", names)
print("Первое имя:", names[0])
print("Последнее имя:", names[-1])

