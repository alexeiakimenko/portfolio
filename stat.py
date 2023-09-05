from wheel import rect, sq, trian

r1 = rect.Rectangle(1, 2)
r2 = rect.Rectangle(3, 4)

s1 = sq.Square(10)
s2 = sq.Square(20)

t1 = trian.Triangle(1, 4, 7)
t2 = trian.Triangle(5, 10, 15)
shape = [r1, r2, s1, s2, t1, t2]
for g in shape:
    print(g.get_per_fig())
