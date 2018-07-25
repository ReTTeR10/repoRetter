
__author__ = 'Мишин Егор Олегович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

# 1ое решение
# #num = "24"
# num = input("Введите целое число: ") # Для диалогового ввода
# i = 0
# max = 0
# while i < len(num):
#     if int(max) <= int(num[i]):
#         max = num[i]
#         i += 1
#     else: i += 1
# print("Самая большая цифра: ", max)

a = int(input("Введите целое число: "))
max_num = 0
if a == 0:
    print(0)
else: pass
while a != 0:
    if max_num < a % 10:
        max_num = a % 10
    else:
        pass
#    print(a % 10, end="  ")
    a = (a - a % 10) // 10

print("Самая большая цифра: ", max_num)



# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

print("\n")
a = int(input("Введите 1-ое число: "))
b = int(input("Введите 2-ое число: "))

b = b + a
a = b - a
b = b - a

print("1ое число после перемены: ", a, " 2-ое число: ", b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

a = int(input("Введите коэффициент а: "))
b = int(input("Введите коэффициент b: "))
c = int(input("Введите c: "))
d = b**2-4*a*c
if d > 0:
    x1 = ((-b) + math.sqrt(d))/(2*a)
    x2 = ((-b) - math.sqrt(d))/(2*a)
    print("x1 = ", x1, " x2 = ", x2)
elif d == 0:
    x1 = -b / 2*a
    print("Уравнение имеет один корень x1 = x2 = ", x1)
elif d < 0:
    print("Действительных (вещественных) корней у уравнения с этим набором коэффициентов не существует")



