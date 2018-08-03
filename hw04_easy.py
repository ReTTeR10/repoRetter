__author__ = 'Мишин Егор Олегович'

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
print('\n Задача 1 - генератор квадрата эл-ов исходного списка\n')
import random


my_list = [random.randint(-10,10) for _ in range(10)]
my_list1 = [elem**2 for elem in my_list]
print('Список 1: ', my_list, '\nСписок 2: ', my_list1)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
