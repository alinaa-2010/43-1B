# словари и множества.{}

# словарь. {} - хранит данные в виде пары,  изменяемый тип данных

# ключ - всегда пишется в начале и в ""
# значение - пишется после ключа, может быть любым типом данных
# student = {"name":"Alina","age":15}
# print(student)
# print(student["name"], student["age"])
# print(student.keys())
# print(student.values())
# print(student.items())

# student["hobby"] = "judo" # - метод добавления
# print(student)

# student["name"] = "bekbolot" # - метод изменения

# student.pop("age") # - метод удаления
# print(student)

# del student["hobby"] # - метод удаления способ 2
# print(student)

# student.pop(("job", "такого ключа нет"))
# print(student)

# множества - {} - самый уникальный тип данных, не содержит дубликат, не имеет определенного порядка, не имеет индексов
# set - множествo - изменяемый {}
# frozenset - множество - не изменяемый

# students = {"Nurbolot","Bekbolot","Askar","Dayan","Aziz"}
# print(students)

# students.add("Abubakir") # добавление элемента
# print(students)
# удаление элемента (2 способа)
# students.remove("Nurbolot") # если нет элемента, то он выдает ошибку
# students.discard("Beksultan") # если нет элемента, то не выдает ошибку
# print("Nuraida" in students) # проверка на наличие элемента

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print(a | b) # обьединение
# print(a & b) # пересечение
# print(a - b) # разность 
# print(a ^ b) # симметричная разность

students = frozenset(["Nurbolot","Bekbolot","Askar","Dayan","Aziz"])
print(students)