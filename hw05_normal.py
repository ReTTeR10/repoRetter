__author__ = 'Мишин Егор Олегович'
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

import os
import easy_module

def program_ui():
    print('\nДобро пожаловать!\n ---- M E N U ----')
    button = input("\n 1 - Перейти в папку\n 2 - Просмотреть содержимое текущей папки"
                   "\n 3 - Удалить папку\n 4 - Создать папку \n Для выхода напишите exit")
    return button



button = ''

while button != 'exit':
    button = program_ui()
    try:
        if button == '1':
            print('Текущая дериктория: ', os.getcwd())
            new_dir = input('Введите желаемую директорию:')
            easy_module.change_dir(new_dir)
            print('Переход выполнен! os.getcwd = ', os.getcwd())
        if button == '2':
            
    print('\n', button)
# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
# easy.py как модуль