__author__ = 'Мишин Егор Олегович'

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

print("\n Задача №1")

equation = 'y = -12x - 11111140.2121'            # Сюда можно подставить соответственно любое уравнение вида y = kx + b
x = 2.5                                          # и все будет работать))
# вычислите и выведите y
print('Уравнение :\n', equation, '\n x = ', x)
if '+' in equation:
    y = float(equation[equation.find('=') + 1:equation.find('x')]) * x + float(equation[equation.find('+') + 1:])
elif '-' in equation:
    y = float(equation[equation.find('=') + 1:equation.find('x')]) * x - float(equation[equation.find('-') + 1:])
print('\n y = ', y)



# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1185'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'
import sys


date = '01.11.1185'



count = 0


if int(date[0:2]) in range(1, 31):
    count += 1
    day = int(date[0:2])
    print('!!1')
else:
    print('Неправильный формат даты, проверьте день')
    sys.exit()
if int(date[3:5]) in range(1, 12):
    month = date[3:5]
    count += 1
    if month == 2 | 4 | 6 | 9 | 11:
        if day != 31:
            count += 1
            print("!!!2")
        else:
            print('Неправильный формат даты, проверьте день')
            sys.exit()
    else:
        pass
else:
    pass
if count == 0:
    print('Неправильный формат датыБ проверьте день/месяц')
    sys.exit()
else:
    pass
if int(date[6:]) in range(1, 10000):
    if len(date[6:]) == 4:
        count += 1
    else:
        pass
if count == 0:
    print('Неправильный формат датыБ проверьте день/месяц')
    sys.exit()
else:
    pass
print('\ncount =', count)
if count == 3:
    print('Дата корректна')
else:
    print('Дата введена некорректно')












# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3