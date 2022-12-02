"""Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k"""

from random import randint

k = int(input('Введите показатель степени полинома k: '))
list_index = []
for index in range(k + 1):
    list_index.append(randint(0,101))

print(list_index)
polinom = []
for num in enumerate(list_index):
    if num[1] != 0:
        index = '' if num[1] == 1 else str(num[1])
        match num[0]:
            case 0:
                polinom.append(str(num[1]))
            case 1:
                polinom.append(index + 'x')
            case _:
                polinom.append(index + 'x^' + str(num[0]))

output_string = ' + '.join(reversed(polinom)) + ' = 0'

print(f'Полином {output_string} будет записан в файл polinom.txt')
f = open('polinom.txt',"w")
f.writelines(output_string)
f.close()
