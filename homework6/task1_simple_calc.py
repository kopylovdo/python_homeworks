"""Программа вычисления арифметического выражения заданного строкой"""
#Используются операции +,-,/,*, приоритет операций стандартный.
OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}
SYMBOLES = ['1','2','3','4','5','6','7','8','9','0','.']

input_string = input('Введите строку выражения, которое нужно вычислить: ')
print(f'Вы ввели выражение {input_string}')

#парсим введенную строку на числа и действия
parsed_string = []
number = ''
for symbol in input_string:
    if symbol in SYMBOLES:
        number += symbol
    elif number:
        parsed_string.append(float(number))
        number = ''
    if symbol in OPERATORS:
        parsed_string.append(symbol)
if symbol:
    parsed_string.append(float(number))

#проверяем наличие отрицательных чисел
if parsed_string[0] == '-':
    parsed_string[1] *= -1
    parsed_string.pop(0)
index = 2
while index < len(parsed_string):
    if parsed_string[index] == '-' and parsed_string[index - 1] in OPERATORS:
        parsed_string[index + 1] *= -1
        parsed_string.pop(index)
    index += 1
#преобразовываем распарсенную строку в обратную польскую нотацию
polish_notation = []
stack = []
for element in parsed_string:
    if element not in OPERATORS:
        polish_notation.append(element)
    else:
        while stack and OPERATORS[element][0] <= OPERATORS[stack[-1]][0]:
            polish_notation.append(stack.pop())
        stack.append(element)
while stack:
    polish_notation.append(stack.pop())

#вычисляем значение
stack = []
for element in polish_notation:
    if element in OPERATORS:
        y, x = stack.pop(), stack.pop()
        stack.append(OPERATORS[element][1](x, y))
    else:
        stack.append(element)

print(f'Результат: {stack[0]}')