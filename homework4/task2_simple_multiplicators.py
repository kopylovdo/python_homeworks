"""Программа, которая составит список простых множителей числа N"""

N = int(input('Введите число N: '))

simple_multiplicators = []
number = N

index = 2
while index ** 2 <= number:
    while number % index == 0:
        if index not in simple_multiplicators:
            simple_multiplicators.append(index)
        number = number / index
    index += 1
if number > 1:
    simple_multiplicators.append(int(number))

print(f'Список простых множителей числа {N} - {simple_multiplicators}')
