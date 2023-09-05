tl = ("ab", "abcd", "cde", "abc", "def")
s = input("s= ")
a = 0
for i in range(len(tl)):
    if s == tl[i]:
        a += 1
if a > 0:
    print("Yes")
else:
    print("No")
