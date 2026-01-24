d1 = { 'a': 10, 'b': 20, 'c': 30, 'd': 40 }

for k,v in d1.items():
    print(f"{k} : {v}")

print(d1.keys()) # dict_keys(['a', 'b', 'c', 'd'])
print(d1.values()) # dict_values([10, 20, 30, 40])
print(d1.items()) # dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])
print(d1.get('a')) # 10
print(d1.get('z')) # None
print(d1.get('z', 100)) # 100

del d1['a']
print(d1)
vl = d1.pop('b')
print(vl)
for key in d1:
    print(key)

for value in d1.values():
    print(value)

for key in d1.keys():
    print(key)

# 6 - Dict
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])

print(f"The alien is {alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(alien_0['x_position'])