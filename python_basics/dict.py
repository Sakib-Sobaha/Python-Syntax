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

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"{key} : {value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

friends = ['sarah', 'phil', 'edward']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language  = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language.title()}")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
for language in set(favorite_languages.values()):
    print(language.title())

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")

    if repeat == 'no':
        polling_active = False

    print("\n---- Poll Results ----")
    for name, response in responses.items():
        print(f"{name} would like to climb {response}.")

