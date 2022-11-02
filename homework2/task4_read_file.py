"""Программа нахождения произведения элементов, на позициях, указанных в файле file.txt"""
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

with open('file.txt','r') as txt_file:
    positions = list(map(int,txt_file.readlines()))

max_index = max(positions)

while True:
    N = int(input('Введите число N '))
    if N < 1:
        print('Введено значение N < 1. Попробуйте ввести N еще раз')
    elif N <= max_index:
        break
    else:
        print(f'Максимальный индекс в файле - {max_index}.\n'
              f'Введенное число {N} больше этого индекса. Попробуйте ввести N еще раз')

input_nums = []
for i in range(N + 1):
    input_nums.append(randint(-N, N))

print('Заданный список', input_nums, 'Список индексов', positions, sep='\n')

product = 1
for pos in sorted(positions):
    if pos <= N:
        product *= input_nums[pos]
    else:
        print(f'Все элементы списка перемножены. Произведение {N}-элемнтов: {product}')
        break
