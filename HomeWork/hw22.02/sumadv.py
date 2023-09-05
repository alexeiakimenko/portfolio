print('Нахождение суммы и среднего арифметического чисел.')
st1 = input('Введите числа через знаки разделители(кроме точки,это воспримется как десятичная дробь): ')
lt1 = list(st1)


def adv(fn):
    def wrap(ch2):
        sk = fn(ch2)
        sra = sk[0] / sk[1]
        print(f'Среднее арифметическое чисел: {st1} = {sra}')

    return wrap


@adv
def slo(ch):
    st2 = ''
    lt2 = []
    for i in ch:

        if 48 <= ord(i) <= 57 or ord(i) == 46:
            st2 += i
        else:
            lt2.append(float(st2))
            st2 = ''
    if st2 != '':
        lt2.append(float(st2))
    summa = sum(lt2)
    print(f'Сумма чисел: {st1} = {summa}')
    return summa, len(lt2)


slo(lt1)
