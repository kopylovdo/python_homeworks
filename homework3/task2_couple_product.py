"""Программа, которая находит произведение пар чисел списка"""
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint

#input = [2, 3, 5, 9, 3]
input_nums = []
n = int(input('Введите количество элементов списка N: '))
half_list = int(n / 2)
for i in range(n):
    input_nums.append(randint(1,21))

product_couples = []

for i in range(1,half_list + 1):
    product_couples.append(input_nums[i-1] * input_nums[-i])
if len(input_nums) % 2 != 0:
    product_couples.append(input_nums[half_list] ** 2)

print(f'Исходный список {input_nums}\nПроизведение пар чисел списка {product_couples}')
