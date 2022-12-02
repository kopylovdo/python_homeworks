"""Модуль просмотра телефонного справочника"""
import utils
import UI

def view_db():
    print('В справочнике найдены следующие записи')
    database = utils.connect_db()
    UI.print_rows(utils.FORMAT)
    for row in database:
        UI.print_rows(list(row.values()))
