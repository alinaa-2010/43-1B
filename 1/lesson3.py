#list - список - дополнительный тип данных, список создаеься через [], совмещает в себе и str, int, float, bool,также является изменяемым типом данных

#name = "nurbolot, adilet, islam"
#student = True
#print(type(student))

#student = ["nurbolot","adilet","islam"]
#print(student)

#numbers = [1,2,3,4,5,6,7]

#result = ["Geeks", 4, True, 5.4,[2,1,3,4,5]] #какие-то знаки (!№%?_) пишутся в кавычках / также можно внутри списка создать еще список
#print(result)

#students = ["nurbolot","adilet","islam","islam"] - можно повторять одни и те же слова, дублировать типо
#print(students)

#students = ["nurbolot","adilet","islam","islam", 5] - индекс наичинается с нуля
#print(students)

#print(students[1]) - так выводят индекс

#print(f"{students[2]} - {students[3]}") - так выводят сразу несколько индексов

#students = ["nurbolot","adilet","islam","islam"] 
#(students)
#students.append("daniel") # append - добавляет элемент в конец списка
#students.append("azamat")
#print(students)
#students.insert(1,"azamat") #добавляет элемент через индекс в определенную позицию
#print(students)
#students.remove("adilet") #удаляет элемент из списка
#students.pop(3) #удаляет по индексу
#print(students)
#students.clear() - удаляет весь список
#print(students)
#students.sort() #сортирует по алфавиту
#print(students)
#students.reverse() #переворачивает список
#print(students)

#tuple - кортеж,создается с помощью круглых скобок (),неизменяемый тип данных в отличии от list
students_list = ["nurbolot","adilet","islam","islam"] #изменяется
student_tuple = ("nurbolot","adilet","islam","islam") #не изменяется + круглые скобки
print(students_list)
print(student_tuple)
#int, float, bool, str - так же как и tuple является неизменяемым



cars = ("bmw","audi","mercedes","tesla","bmw")
print(cars)
test = list(cars)
print(test)
test.remove("mercedes")
test.pop(3)
print(test)

cars = tuple(test)
print(cars)