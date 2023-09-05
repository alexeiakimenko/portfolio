import json
from random import choice, randint


def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'g', 'm', 'n', 'k']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    person = {
        'name': name,
        'tel': tel
    }
    return person


def write_json(person_dict):
    key = ''
    for i in range(5):
        key += chr(randint(97, 122))

    try:
        data = json.load(open('dicindic.json'))
    except FileNotFoundError:
        data = {}
    data[key] = person_dict
    with open('dicindic.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())
