"""Cписок чисел Фибоначчи, в том числе для отрицательных индексов, для заданного числа"""

def calculate_fibonachi(n):
    '''Fibonachi list calculation method'''
    if 0 <= n <= 1:
        return n
    elif n > 1:
        return calculate_fibonachi(n - 1) + calculate_fibonachi(n - 2)
    elif n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return calculate_fibonachi(n + 2) - calculate_fibonachi(n + 1)

k = int(input('Введите число k: '))
fibonachi_list = []
for num in range(-k, k + 1):
    fibonachi_list.append(calculate_fibonachi(num))

print(fibonachi_list)
