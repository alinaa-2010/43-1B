#задача 1
numbers = [5, 10, 15, 20, 25]
numbers.append(30)
numbers.insert(1, 7)
numbers.remove(15)
print(numbers)

#задача 2 
numbers = [10, 3, 7, 1, 9]
numbers.sort()
numbers.reverse()
print(numbers)
print(max(numbers))
print(len(numbers))

#задача 3
names = ["Alina", "Bek", "Ali"]
names.append("Daniyar")
names.append("Aida")
print(names)
names.remove("Bek")
names.pop(3)
print(names)

#задача 4
cars = ["BMW", "Audi", "Tesla", "Lexus"]
cars.insert(0, "Mercedes")
print(cars)
cars.remove("Tesla")
cars.sort()
print(cars)

#задача 5
cities = ("Osh", "Astana", "Bishkek", "Moscow")
print(cities[0])
print(cities[3])
print(len(cities))

#задача 6
nums = (5, 10, 15, 20)
print(nums)
test = list(nums)
test.append(25)
nums = tuple(test)
print(nums)