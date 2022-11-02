"""Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму"""

digits = []

N = int(input('Введите число N '))

for i in range(1,N + 1):
    digits.append((1 + 1 / i) ** i)

print(sum(digits))
