"""Прогамма, вычисляющая сумму многочленов, каждый из которых хранится в файле"""

from collections import Counter

def parse_polinome(polinom):
    '''Parsing list of polinom indexes as str into dict with quality as key and index as value'''
    polinom_index = {}
    for part in polinom:
        if part.partition('x^')[1]:
            polinom_index[int(part.partition('x^')[2])] = int(part.partition('x^')[0])
        elif part.partition('x')[1]:
            polinom_index[1] = 0 if not part.partition('x')[0] else (int(part.partition('x')[0]))
        else:
            polinom_index[0] = int(part)
    return polinom_index

with open('polinom_1.txt','r') as first_file:
    first_polinom_string = first_file.read()

with open('polinom_2.txt','r') as second_file:
    second_polinom_string = second_file.read()

first_polinom = first_polinom_string[:-4].split(' + ')
second_polinom = second_polinom_string[:-4].split(' + ')

print(first_polinom,second_polinom)

first_polinom_index = parse_polinome(first_polinom)
second_polinom_index = parse_polinome(second_polinom)

sum_polinom = dict(reversed(sorted((Counter(first_polinom_index) + Counter(second_polinom_index)).items())))

output_polinom = []
for key in sum_polinom:
    if sum_polinom[key] != 0:
        index = '' if sum_polinom[key] == 1 else str(sum_polinom[key])
        match key:
            case 0:
                output_polinom.append(str(sum_polinom[key]))
            case 1:
                output_polinom.append(index + 'x')
            case _:
                output_polinom.append(index + 'x^' + str(key))

output_string = ' + '.join(output_polinom) + ' = 0'

print(f'Первый полином: {first_polinom_string}\n'
      f'Второй полином: {second_polinom_string}\n'
      f'Сумма полиномов: {output_string}\nБудет сохранена в файл polinom_sum.txt')

f = open('polinom_sum.txt',"w")
f.writelines(output_string)
f.close()
