tl = ("ab", "abcd", "cde", "abc", "def")
s = input("s= ")

try:
    if tl.index(s) >= 0:
        print("Yes")
except ValueError:
    print("No")
