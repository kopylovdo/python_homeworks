"""Модуль импорта данных в справочник"""
import utils
import UI

items = utils.FORMAT

def insert_string():
    print('Вы находитесь в разделе внесения новой строки в телефонный справочник')
    input_string = dict.fromkeys(items)
    input_string['id'] = str(len(utils.connect_db()) + 1)
    for colomn in items[1:len(items)]:
        input_string[colomn] = input(f'Введите значение поля {colomn}: ')
    print(f'Вы хотите добавить строку {input_string}?')
    if UI.confirm_action():
        utils.update_data(input_string)
        print(f'Строка {input_string} успешно добавлена')
