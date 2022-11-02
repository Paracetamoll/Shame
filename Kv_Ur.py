import math

# -1 (нет корней)
# -2 (try except)
# -3 (inf)
# -4(+-)

const = {'pi': math.pi,
         '-pi': -math.pi,
         'e': math.e,
         '-e': -math.e,
         'inf': math.inf,
         '-inf': -math.inf}

'''
def is_num(s):
    try:
        float(s)
        return True
    except ValueError:
        if s in const:
            return True
        else:
            return False
'''


def is_num(s):
    st = s.split('.')
    if st[0][0] == '-':
        st[0] = st[0][1:]
        if len(st) == 1 and (st[0].isdigit() or st[0] in const):
            return True
        elif len(st) == 2 and st[0].isdigit() and st[1].isdigit():
            return True
        else:
            return False
    else:
        if len(st) == 1 and (st[0].isdigit() or st[0] in const):
            return True
        elif len(st) == 2 and st[0].isdigit() and st[1].isdigit():
            return True
        else:
            return False

a = input('Коэфициент a:')
b = input('Коэфициент b:')
c = input('Коэфициент c:')
if is_num(a) and is_num(b) and is_num(c):
    if a in const:
        a = const[a]
    else:
        a = float(a)
    if b in const:
        b = const[b]
    else:
        b = float(b)
    if c in const:
        c = const[c]
    else:
        c = float(c)

    d = b ** 2 - 4 * a * c

    if a != 0 and c != 0:
        if d > 0:
            print('x1 =', (-b + math.sqrt(d)) / (2 * a))
            print('x2 =', (-b - math.sqrt(d)) / (2 * a))
        if d == 0:
            print('Оба корня совпадают в точке', -b / (2 * a))
        if d < 0:
            kor = math.sqrt(-d)
            print('x1 =', (-b) / (2 * a), '+ (' + str(kor / (2 * a)) + 'i)')
            print('x2 =', (-b) / (2 * a), '- (' + str(kor / (2 * a)) + 'i)')

    elif a == 0 and b != 0:
        print('x1 =', -c / b)
        print('x2 =', -c / b)

    elif a == 0 and b == 0 and c == 0:
        print('Корнем является множество всех чисел')

    elif a == 0 and b == 0 and c != 0:
        print('Корней нет')

    elif a != 0 and b == 0 and c == 0:
        print('x1 = 0')
        print('x2 = 0')

    elif a != 0 and b != 0 and c == 0:
        d = b**2
        print('x1 =', (-b + math.sqrt(d)) / (2 * a))
        print('x2 =', (-b - math.sqrt(d)) / (2 * a))

else:
    print('Должны быть введены числа')
