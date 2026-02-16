a = [10,20,30,40]

print(a.count(10))

print(a.pop())

a.append(50)
print(a)
print(a.index(30))

a.insert(2,25)
print(a)

a.remove(20)
print(a)

a.sort()
print(a)

a.reverse()
print(a)

a.clear()
print(a)

############################
### Chapter 3 & 4  #########
############################

cars = ['bmw', 'toyota', 'toyota', 'audi', 'subaru']
print(cars)

cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars.sort(key=str.lower)
print(cars)

# sorting a list temporarily
print(sorted(cars))
print(cars)

print(len(cars))

for car in cars:
    print(car)
    print(f"{car.upper()} is {car.upper()}")

numbers = list(range(10))
print(numbers)

even_numbers = list(range(2, 11, 2))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# List comprehension
squares = [value**2 for value in range(1,11)]
print(squares)

# Slicing a list
players = ['messi', 'neymar', 'ronaldo', 'kortoa', 'ramos']
print(players[0:3]) # ['messi', 'neymar', 'ronaldo']
print(players[:3])
print(players[-3:]) # ['ronaldo', 'kortoa', 'ramos']
print(players[::-1]) # ['ramos', 'kortoa', 'ronaldo', 'neymar', 'messi']
print(players[1:4])