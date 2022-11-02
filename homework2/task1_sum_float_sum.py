"""Программа, которая принимает на вход вещественное число и показывает сумму его цифр"""
input_number = input('Введите число ')
sum_digits = 0
for digit in enumerate(input_number):
    if digit[1] not in (',','.','-'):
        sum_digits += int(digit[1])
print(f'Сумма цифр введенного числа: {sum_digits}')
