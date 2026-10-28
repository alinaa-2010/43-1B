#задача 1
user = {
    "login": "alina123",
    "password": "012345",
    "age": 15
}

user["password"] = "newpass123"
user["city"] = "Bishkek"
del user["age"]
print(user)

#задача 2
products = {
    "apple": 50,
    "banana": 30,
    "milk": 60,
    "bread": 35
}

deleted = products.pop("milk") 
print("Удалённое значение:", deleted)
print("Обновлённый словарь:", products)

#задача 3
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)

#задача 4
names = ["Aibek", "Nurbek", "Aibek", "Azamat", "Nurbek", "Aigerim"]

names_set = set(names)
print(names_set)

names_set.add("Alina")
print(names_set)

print("Azamat" in names_set)

names_set.remove("Aigerim")
print(names_set)