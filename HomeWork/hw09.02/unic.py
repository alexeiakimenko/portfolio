str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
set1 = set(str1)
set2 = set(str2)
set3 = set1 ^ set2
print("Искомыми буквами являются:", set3)
