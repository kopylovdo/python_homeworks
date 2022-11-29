"""Программа вычисления арифметического выражения заданного строкой c возможностью использования скобок, меняющих приоритет операций"""
#Используются операции +,-,/,*.
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
    if symbol in OPERATORS or symbol in '()':
        parsed_string.append(symbol)
if symbol:
    parsed_string.append(float(number))
print(parsed_string)
#проверяем наличие отрицательных чисел
if parsed_string[0] == '-':
    parsed_string[1] *= -1
    parsed_string.pop(0)
index = 1
while index < len(parsed_string):
    last = parsed_string[index-1]
    if parsed_string[index] == '-' and (last in OPERATORS or last == '('):
        parsed_string.pop(index)
        parsed_string[index] *= -1 
    index += 1

print(parsed_string)
#преобразовываем распарсенную строку в обратную польскую нотацию
polish_notation = []
stack = []
for element in parsed_string:
    if element in OPERATORS:
        while stack and stack[-1] != '(' and OPERATORS[element][0] <= OPERATORS[stack[-1]][0]:
            polish_notation.append(stack.pop())
        stack.append(element)
    elif element == ')':
        while stack:
            x = stack.pop()
            if x == '(':
                break
            polish_notation.append(x)
    elif element == '(':
        stack.append(element)
    else:
        polish_notation.append(element)

while stack:
    polish_notation.append(stack.pop())

print(polish_notation)
#вычисляем значение
stack = []
for element in polish_notation:
    if element in OPERATORS:
        y, x = stack.pop(), stack.pop()
        stack.append(OPERATORS[element][1](x, y))
    else:
        stack.append(element)

print(f'Результат: {stack[0]}')
