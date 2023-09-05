dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic_all = dic1.copy()
dic_all.update(dic2)
dic_all.update(dic3)
print(dic_all)
