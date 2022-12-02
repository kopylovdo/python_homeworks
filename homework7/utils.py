"""Утилиты телеонного справочника"""
import json

FORMAT = ('id','name', 'surname','birthday','workat','phone')

def connect_db():
    """получение данных из файла"""
    with open('db.json','r') as db_file:
        database = json.load(db_file)
    return database

def save_data(data):
    """сохранение данных в файла"""
    with open('db.json','w') as db_file:
        json.dump(data, db_file)

def update_data(data):
    database = connect_db()
    database.append(dict(data))
    save_data(database)
