"""контроллер телефонного справочника"""
import UI
import editor
import viewer
import utils

controller_menu = ('Выход','Просмотр справочника','Внесение новых данных')

def run():
    print('Телефонный справочник')
    user_select = -1
    while user_select != 0:
        print('Вы находитесь в главном меню')
        user_select = UI.menu_select(controller_menu)
        match user_select:
            case 1:
                viewer.view_db()
            case 2:
                editor.insert_string()
