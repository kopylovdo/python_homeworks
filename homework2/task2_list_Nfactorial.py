"""Программа, которая принимает на вход число N и выдает набор произведений чисел от 1 до N"""

def factorial(n):
    '''Calculate factorial'''
    result = 1
    for i in range(n):
        result *= i + 1
    return result

N = int(input('Введите число N '))
print(*(factorial(index + 1) for index in range(N)),sep=', ')
