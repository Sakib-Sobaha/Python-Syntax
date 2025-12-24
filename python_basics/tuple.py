tup = (10, 20, 30, 40)

print(tup.count(10))

print(tup.index(30))

for x in tup:print(x)
# tup.append(50) # AttributeError: 'tuple' object has no attribute 'append'

# tup.remove(20) # AttributeError: 'tuple' object has no attribute 'remove'
# tup.sort() # AttributeError: 'tuple' object has no attribute 'sort'
# tup.reverse() # AttributeError: 'tuple' object has no attribute 'reverse'
# tup.clear() # AttributeError: 'tuple' object has no attribute 'clear'
# tup.insert(2,25) # AttributeError: 'tuple' object has no attribute 'insert'
# tup.pop() # AttributeError: 'tuple' object has no attribute 'pop'
# tup.extend([50,60]) # AttributeError: 'tuple' object has no attribute 'extend'
# tup[0] = 100 # TypeError: 'tuple' object does not support
# tup[1:3] = [200,300] # TypeError: 'tuple' object does not support item assignment
# del tup[0] # TypeError: 'tuple' object doesn't support item deletion
