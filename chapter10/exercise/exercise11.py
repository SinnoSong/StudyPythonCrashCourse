import json


def write_favorite_number(filename, number):
    with open(filename, 'w') as f:
        json.dump(number, f)


def read_favorite_number(filename):
    with open(filename, 'r') as f:
        return json.load(f)


number = input("Your favorite number?")
write_favorite_number('favorite_number.json', number)
print(read_favorite_number('favorite_number.json'))
