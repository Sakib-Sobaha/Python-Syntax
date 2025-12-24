def fun(*args):
    return sum(args)

print(fun(20,30,40))

def gun(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')


gun(name="John", age=25, city="New York")

def mult(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(mult(2,3,4,5))

def introduce(**kwargs):
    d = []
    for key, value in kwargs.items():
        d.append(f"{key} is {value}")
    return ", ".join(d)


print(introduce(name="Alice", age=30, city="Los Angeles"))
        