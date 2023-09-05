import os

p = r'E:\учёба\python'
lst = os.listdir(p)
s = []
for i in lst:
    s.append(os.path.join(p, i))
k = 0
while k < len(s):
    if os.path.isdir(s[k]):
        print(f'{lst[k]} - dir.')
    if os.path.isfile(s[k]):
        print(f'{lst[k]} - file - {os.path.getsize(s[k])} bytes.')
    k += 1
