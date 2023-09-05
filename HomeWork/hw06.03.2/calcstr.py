file_hw = 'test.txt'
with open(file_hw, 'r', encoding='UTF-8') as f:
    lst = f.readlines()

lines = 0
word = 0

while lines < len(lst):
    vlt = lst[lines].split(' ')
    symbol = len(lst[lines])
    for i in vlt:

        if 1040 <= ord(i[0]) <= 1103 or ord(i[0]) == 1025 or ord(i[0]) == 1105:
            word += 1

    print(f'{lines + 1} строка : слов - {word} ; символов {symbol - 1}')
    word = 0

    lines += 1
print(f'Количество строк - {len(lst)}.')
