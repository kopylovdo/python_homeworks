"""Модуль импорта данных в справочник"""
import utils
import viewer
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

def delete_row():
    print('Вы находитесь в разделе удаления строк')
    viewer.view_db()
    row = int(input('Введите id строки, которую требуется удалить: ')) - 1
    data = utils.connect_db()
    print(f'Вы хотите удалить строку {data[row]}?')
    if UI.confirm_action():
        data.pop(row)
        utils.update_data(data)
        print(f'Строка {row} успешно удалена')
