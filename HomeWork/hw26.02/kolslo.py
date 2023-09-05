st = '''
Ежевику для ежат
Принесли два ежа.
Ежевику еле-еле
Ежата возле ели съели.
'''
print(st)
st = st.split()

kol = 0

i = 0
while i < len(st):
    if st[i][0].lower() == 'е':
        kol += 1
    i += 1
print(f'Количество слов: {kol}')
