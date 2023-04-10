friend3 = {'first_name': "xc", 'last_name': 's', 'age': 24, 'city': "123"}
friend1 = {'first_name': "xc1", 'last_name': 's', 'age': 24, 'city': "123"}
friend2 = {'first_name': "xc2", 'last_name': 's', 'age': 24, 'city': "123"}

people = [friend1, friend2, friend3]
for friend in people:
    print(friend['first_name'])
    print(friend['last_name'])
    print(friend['age'])
    print(friend['city'])
