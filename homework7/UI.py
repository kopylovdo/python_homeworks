"""Модуль интерфейса взаимодействия с пользователем"""

def menu_select(menu_items):
    """выбор действия пользователя"""
    answer = -1
    while answer < 0:
        print('Список доступных действий')
        for num in enumerate(menu_items):
            print(f'{num[0]} - {num[1]}')
        answer = int(input('Что вы хотите сделать?: '))
        if 0 <= answer < len(menu_items):
            break
        else:
            answer = -1
    return answer

def confirm_action():
    """подтверждение на изменение данных"""
    answer = ''
    while not answer:
        answer = input('Подтвердить внесение изменений (Y/n): ')
        if answer in ('Yn'):
            break
        else:
            answer = ''
    return True if answer == 'Y' else False

def print_rows(data):
    print(' | '.join(data))
    print('-' * 60)
