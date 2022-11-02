"""Определение номера четверти плоскости по координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0"""

x = 0
y = 0

#цикл для проверки того, что пользователь не ввел точку (0,0)
while x == 0 and y == 0:
    #стараюсь соблюдать PEP8 и ограничивать строку 80 символами
    #поэтому в следующей строке добавился print() перед input()
    print('Введите координаты точки (X ≠ 0 и Y ≠ 0) через пробел:',end=" ")
    x,y = map(float,(input().split(sep=' ')))

#определяем четверть или ось на которой находится заданная точка
if x == 0 or y == 0:
    quater_num = 'на оси Х' if x * y == 0 and y == 0 else 'на оси Y'
elif x * y > 0:
    quater_num = 1 if x > 0 else 3
else:
    quater_num = 2 if y > 0 else 4

if not isinstance(quater_num,str):
    quater_num = f'в {quater_num}-й плоскости'

print(f'Точка ({x};{y}) лежит {quater_num}')
