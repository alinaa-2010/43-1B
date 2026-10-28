# функции

# 1) встроенные функции
# 2) пользовательские функции
# 3) анонимные функции

# 1) встроенные функции
# print("hello world")
# input()
# len
# min
# max
# count

# 2) пользовательские функции

# def name(): 
#    print("hello alina")

# name()

# def summa(num1,num2):
#    print(num1 + num2)
#
# summa(5, 2)

# 3) анонимные функции 
# result = lambda num1, num2: num1 + num2
# print(result(6,3))

# print((lambda num1, num2: num1 + num2)(6,3))

# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#    numbers[num-1] *= 2
#
# result = list(map(lambda num: num*2, numbers))
# print(result)

# map - альтернативная версия цикла которая выполняет итерации (круги)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

result = list(filter(lambda num: num % 2 == 0, numbers))
print(result)