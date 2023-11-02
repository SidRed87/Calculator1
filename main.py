print ('Калькулятор')
what = input('Оберіть операцію? (+,-,:,*)')
a = float( input('Введіть число 1: '))
b = float( input('Введіть число 2: '))


if what == "+":
    c = a + b
    print('=' + str(c))
elif what == "-":
    c = a - b
    print('=' + str(c))
elif what == ":":
    c = a / b
    print('=' + str(c))
elif what == "*":
    c = a * b
    print('=' + str(c))
else:
    print('Обрана невірна операція')