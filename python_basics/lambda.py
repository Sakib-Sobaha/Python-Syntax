s1 = "Guido van Rossum"
s2 = lambda s: s.upper()
print(s2(s1))

n = lambda x : "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(10))

check = lambda x : "Even" if not (x%2) else "Odd"
print(check(10))