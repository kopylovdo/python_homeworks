"""Алгоритм перемешивания списка"""

import random

input_list = input('Введите список элементов, разделенных пробелами\n').split()

#вводим дополнительную переменную, чтобы исходный список не изменился
output_list = input_list

random.shuffle(output_list)
print(output_list)
