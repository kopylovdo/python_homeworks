"""Программа, которая будет преобразовывать десятичное число в двоичное"""

decimal_number = int(input('Введите число: '))
input_number = decimal_number
binary_num = [] if input_number != 0 else [0]

while decimal_number / 2 != 0:
    binary_num.insert(0, decimal_number % 2)
    decimal_number = int(decimal_number / 2)

if input_number < 0:
    binary_num.insert(0, '-')

print('Десятичное число',input_number,'в двоичном коде:',''.join(map(str,binary_num)))
