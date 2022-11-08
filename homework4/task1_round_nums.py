"""Программа, которая вычисляет число c заданной точностью d"""
from decimal import Decimal

number = Decimal(input('Введите число: '))

while True:
    quantity = input('Введите точность округления d в диапазоне [10^(-1) ≤ d ≤10^(-10)]: ')
    if 1 / float(quantity) % 10 == 0 and quantity.count('0') in range(1,11):
        break

output_number = number.quantize(Decimal("1." + '0' * quantity.count('0')))
print(f'Число {number} с точностью {quantity}= {output_number}')
