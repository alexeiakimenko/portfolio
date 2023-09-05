file_hw = r'E:\учёба\python\two.txt'
with open(file_hw, 'r') as f:
    lst = f.readlines()
    i = len(lst)

with open(file_hw, 'w') as f:
    while i > 0:
        i = i - 1
        f.write(lst[i])

