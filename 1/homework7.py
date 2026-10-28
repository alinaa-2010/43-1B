# задание 1
def sum_positive(numbers):
    summa = 0
    for num in numbers:
        if num > 0:
            summa += num
    return summa

print(sum_positive([5, -2, 10, -7, 3]))  
# задание 2
def glasnye(text):
    vowels = "аеёиоуыэюя"
    count = 0
    
    for letter in text:
        if letter in vowels:
            count += 1
            
    return count

print(glasnye("Привет мир"))
# задание 3
numbers = [2, 5, 8, 11, 14, 17, 20]
result = list(map(lambda x: x + 10, numbers))
print(result)

# задание 4
nums = [3, 6, 9, 12, 15, 18, 21]
result = list(filter(lambda x: x % 3 == 0 and x > 10, nums))
print(result)