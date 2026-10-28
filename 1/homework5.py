# задача 1
n = int(input("Введите число: "))
while n >= 1:
    print(n)
    n -= 1

# задача 2 
numbers = [12, 7, 9, 20, 3, 15]
for num in numbers:
    if num > 10:
        print(num)

# задача 3
n = int(input("Введите число: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print(count)

# задача 4
summa = 0
while True:
    n = int(input("Введите число: "))
    if n == 0:
        break
    summa += n
print("Сумма:", summa)