s = ['1','2','3']
res = map(int, s)
print(list(res))


def double(x):
    return x**2

a = [1,2,3,4,5]
r = map(double, a)
print(list(r))


r1 = list(map(lambda x: x**3, a))
print(r1)


b = [10,20,30,40,50]
r2 = list(map(lambda x, y: x+y, a, b))
print(r2)