dic = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}
for k in dic:
    print(k)
    for k2 in dic[k]:
        print(k2, ":", dic[k][k2])
dic['emp3']['salary'] = 8500
for k in dic:
    print(k)
    for k2 in dic[k]:
        print(k2, ":", dic[k][k2])