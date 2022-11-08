"""Программа, определяющая разницу между максимальным и минимальным значением дробной части элементов."""
from random import uniform

#input = [2, 3, 5, 9, 3]
input_nums = []
n = int(input('Введите количество элементов списка N: '))
for i in range(n):
    input_nums.append(round(uniform(1.00,11.00),2))

fractional_list = []
for num in enumerate(input_nums):
    fractional_list.append(round(num[1] % 1,2))

delta = max(fractional_list) - min(fractional_list)

print(f'Исходный список\n{input_nums}\n'
      f'Разницу между максимальным и минимальным значением дробной части: {delta}')
