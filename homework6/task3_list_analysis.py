"""Программа, определяющая списки уникальных и список повторяемых элементов и последовательность без дубликатов"""

from random import randint

N = int(input('Введите количество элементов последовательности N: '))

nums = []
for index in range(N + 1):
    nums.append(randint(0,11))

result = {index: nums.count(index) for index in nums}
all_nums = list(result.keys())
uniq_nums = [index for index in list(result.keys()) if result[index] == 1]
multi_nums = [index for index in list(result.keys()) if result[index] > 1]

print(f'Исходная последовательность {nums}')
print(f'Последовательность без дубликатов {all_nums}')
print(f'Уникальные элементы {uniq_nums}')
print(f'Повторяющиеся элементы {multi_nums}')
