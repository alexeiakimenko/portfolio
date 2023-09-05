li = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]

for i in range(len(li)):
    vs = 0
    for j in range(len(li)):
        if li[i] == li[j]:
            vs += 1
    if vs == 1:
        print(li[i], end=" ")
