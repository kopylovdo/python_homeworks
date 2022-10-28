"""проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат"""

def is_true(arg_x,arg_y,arg_z):
    left = not (arg_x or arg_y or arg_z)
    right = not arg_x and not arg_y and not arg_z
    return left == right

print('\nТаблица истинности \n\nX | Y | Z | res\n----------------')
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, z, is_true(x,y,z), sep=' | ')
            print('----------------')
