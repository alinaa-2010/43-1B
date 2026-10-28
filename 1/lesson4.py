#циклы - повторение действия
#print("Hello world")
#print("Hello world")
#print("Hello world")
#print("Hello world")
#print("Hello world")
#print("Hello world")
#print("Hello world")
#print("Hello world")
#print("Hello world")
#print("Hello world")

#for - для
#while - пока

#цикл с диапазоном
#for i in range(10):
#    print("Hello world")

#цикл с итерацией
#students = ["nurbolot","adilet","islam","Askar"] 
#for result in students:
#     print("Привет", result)
 
#name = "Alina"
#for lett in name:
#    print(lett +  " " + "hell")

#numbers = [3, 2, 5, 7, 2, 1]
#for otvet in numbers:
#    print(otvet *2)

#for num in range(30, 101):
#    print(num)

#num = 0
#while True
#   num += +999999
#   print(num)

#while True:
#    num = int(input("Введите число:"))
#    if num % 2 == 0:
#        print("Четное")
#    else:
#        print("Нечетное")

#try:
#    num1 = int(input("Введите первое число: "))
#    num2 = int(input("Введите второе число: "))
#    try:
#       print(num1 / num2)
#    except ZeroDivisionError:
#        print("На ноль делить нельзя! Попробуйте еще раз.")
#except:
#    print("Вы ввели не число!")

try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    try:
            print(num1 / num2)
    except ZeroDivisionError:
            print("На ноль делить нельзя")

except ValueError:
       print("Ошибка! Введите целое число")



