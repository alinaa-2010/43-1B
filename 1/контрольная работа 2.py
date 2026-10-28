# задание 1
student = {
    "name": "Аlina",
    "age": 15,
    "group": "39-1B",
    "средний балл": "неизвестно"
}
print(student)
print("Имя:", student["name"])
print("Средний балл:", student["средний балл"])

# задание 2
products = {
    "bread": 30,
    "milk": 60,
    "chocolate": 100,
    "cheese": 250,
    "tea": 80
}
print(products)
max_product = max(products, key=products.get)
min_product = min(products, key=products.get)

average_price = sum(products.values()) / len(products)

print("Самый дорогой:", max_product, products[max_product])
print("Самый дешевый:", min_product, products[min_product])
print("Средняя цена:", average_price)
# задание 3
words = set()

for i in range(5):
    word = input("Введите слово: ")
    words.add(word)

print("Уникальные слова:", words)
print("Количество уникальных слов:", len(words))
# задание 4
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a & b)
print(a - b)
print(b - a)
print(a | b)

# задание 5
students = {
    "Alina": [5, 4, 5],
    "Nurbolot": [3, 4, 4],
    "Marat": [5, 5, 5]
}

for name in students:
    sr_ball = sum(students[name]) / 3
    print(name, sr_ball)

# задание 6
text = input("Введите строку: ")
letters = {}

for i in text:
    if i in letters:
        letters[i] = letters[i] + 1
    else:
        letters[i] = 1

print(letters)

# задание 7
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
num = list(set(numbers))
print(num)

# задание 8 
student1 = {"math", "english", "history", "biology"}
student2 = {"math", "physics", "english", "geography"}

print(student1 & student2)
print(student1 - student2)
print(student2 - student1)

# задание 9
nums = [2, 4, 6, 8]
result = list(map(lambda x: x**2, nums))
print(result)

# задание 10
n = int(input("Введите число: "))

for i in range(1, 11):
    print(n, "*", i, "=", n * i)
