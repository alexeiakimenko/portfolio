file_hw = r'E:\учёба\python\text2.txt'

with open(file_hw, 'r') as f:
    lst = f.readlines()

while True:
    pos1 = int(input('Введите номер строки которую хотите заменить: '))
    pos2 = int(input('Введите номер строки на которую хотите заменить: '))
    if 1 < pos1 > 3 or 1 < pos2 > 3:
        print('Номер одной или двух строк не существует!')
    elif pos1 == pos2:
        print('Введите разные строки!')
    else:
        break
with open(file_hw, 'w') as f:
    lst[pos1 - 1], lst[pos2 - 1] = lst[pos2 - 1], lst[pos1 - 1]
    f.writelines(lst)



