"""Программа, которая находит сумму элементов списка, стоящих на нечётной позиции"""
from random import randint

input_nums = []
n = int(input('Введите количество элементов списка N: '))
for i in range(n):
    input_nums.append(randint(0,20))
sum_nechet_pos = sum(input_nums[1::2])
print(f'Сумма элементов списка {input_nums} на нечтных позициях: {sum_nechet_pos}')
