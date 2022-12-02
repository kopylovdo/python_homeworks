"""Программа, которая выведет список неповторяющихся элементов исходной последовательности"""

from random import randint

N = int(input('Введите количество элементов последовательности N: '))

nums = []
for index in range(N + 1):
    nums.append(randint(0,20))

uniq_nums = []
for num in nums:
    if nums.count(num) == 1:
        uniq_nums.append(num)

print(f'Уникальные элементы последовательности {nums} - {uniq_nums}')
