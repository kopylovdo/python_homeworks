"""Программа, принимающая цифру дня недели, проверяет, является ли он выходным"""

day_num = int(input('Проверим, является ли день выходным. Введите цифру его обозначающую '))
print('Да' if day_num in range(6,8) else 'Нет' if day_num in range(1,6) else 'Это не день недели')
