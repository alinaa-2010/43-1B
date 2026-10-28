# задание 1
with open("students.txt", "w") as file:
    file.write("Alina\n")
    file.write("Nurbek\n")
    file.write("Bekbolot\n")
    file.write("Ruslan\n")
    file.write("Elvira\n")

with open("students.txt", "r") as file:
    students = file.readlines()

print("First:", students[0].strip())
print("Last:", students[4].strip())

with open("students.txt", "a") as file:
    file.write("Daniyar\n")
    file.write("Aziz\n")

with open("students.txt", "r") as file:
    print("\nAll students:")
    print(file.read())

# задание 2
import os
num1 = int(input("Введите первое число:"))
num2 = int(input("Введите второе число:"))
num3 = int(input("Введите третье число:"))
print(num1 + num2 + num3)

write_file = open("numbers.txt", "w")
write_file.write(f"{num1} + {num2} + {num3} = {num1 + num2 + num3}\n")
write_file.close()

write_file = open("numbers.txt", "r")
numbers = write_file.read().splitlines()
write_file.close()

parts = numbers[0].split()
summa = int(parts[0]) + int(parts[2]) + int(parts[4])
print("Сумма чисел:", summa)

os.remove("numbers.txt")
