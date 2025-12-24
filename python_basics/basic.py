print('Hello World')
# name = input("Enter something: ")
# print("Hello, ", name, "! Welcome")

s = "Bob"
print(s)

s = "Alice"
age = 25
city = "New York"
print(s, age, city)

# x, y = input("Enter numbers: ").split()
# print("Number of boys: ",x)
# print("Number of girls: ",y)

# color = input("What color is rose")
# print(color)


# n = int(input("How many roses?: "))
# print(n)

# price = float(input("Price for each rose: "))
# print(price)

tpl = (12,14,16)
lst = ["penta", "hexa", "hepta"]
dic = {"x":1, "y":2, "z":3}

print(type(tpl))
print(type(lst))
print(type(dic))


a = b = c = 100
print(a,b,c)

x,y,z = 1,2.5,"minku"
print(x,y,z)


a = 2
b = 5
print(a > b, a < b, a == b, a != b, a >= b, a <= b)

print(a + b, a - b, a * b, a / b, a // b, a % b, a ** 2)

# bitwise operators
p = 60  # 0011 1100
q = 13  # 0000 1101
print(p & q, p | q, p ^ q, ~p, p << 2, p >> 2)

# Assignment operators
a = 10
a += 5
print(a)
a -= 3
print(a)
a *= 2
print(a)
a /= 4
print(a)
a //= 2
print(a)
a %= 3
print(a)            
a **= 3
print(a)
# a &= 2
# print(a)
# a |= 4
# print(a)
# a ^= 3
# print(a)

x = 24
y = 20
list = [10, 20, 30, 40, 50, 60]

if (x not in list):
    print("x is absent from the list")
else:
    print("x is present in the list")

if (y in list):
    print("y is present")
else:
    print("y is absent")

# Ternary operator
a,b = 10,20
min = a if a < b else b 

import keyword

print("keywords list : ")
print(keyword.kwlist)
x = keyword.kwlist
for y in x:
    print(y)

a = [1,2,3,4,5,6,6,6,6,2,3,4]

tup1  = tuple(a)
for x in tup1:
    print(x)

s1 = set(a)
for x in s1:
    print(x)

print(s1)

# Dictionary
dic = {"name":"Alice", "age":25, "city":"New York"}
for x in dic:
    print(x, dic[x])

print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.get("name"))

cube_l = lambda x : x**3
print(cube_l(3))