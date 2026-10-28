# Работа с файлами

# без with
# с with

# 1 - r - read - читать содержимое файла
# 2 - w - write - перезапись
# 3 - a - append - добавление

# file = open('geeks.txt',"r")
# result = file.read
# print(result)
# file.close()

# num1 = int(input("Введите первое число:"))
# num2 = int(input("Введите второе число:"))
# print(f"{num1} + {num2} = {num1 + num2}")

# write_file = open("result.txt", "w")
# write_file.write(f"{num1} + {num2} = {num1 + num2}\n")
# write_file.close

# write_file = open("result.txt", "a")
# write_file.write(f"{num1} + {num2} = {num1 + num2}\n")
# write_file.close

with open("result.txt","r") as result_file:
    result = result_file.read()
    print(result)

with open("result.txt","w") as result_file:
    result = result_file.write("Hello world\n")

import os
os.remove("result.txt")