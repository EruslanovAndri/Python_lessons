from pathlib import Path
from data_base import *


def my_list_To_string(db: list[str]):
    for i in range(len(db)):
        for j in range(len(db[i])):
            my_string = ''.join(db)
    return my_string


def my_string_To_list(db: list[str]):
    my_list = []
    for i in range(len(db)):
        for j in range(len(db[i])):
            temp_str = db[i][j].replace('\n',' ')
            my_list.append(''.join(temp_str))
    return my_list


def export_data_base_txt_format(db: list[str]):
    str_data_for_export = my_list_To_string(db)
    export_data = Path('export_data.txt')
    with open(export_data, 'w') as export_data:
        export_data.write(str_data_for_export)
    return str_data_for_export

def export_data_base_csv_format(db: list[str]):
    str_data_for_export = my_list_To_string(db)
    export_data = Path('export_data.scv')
    with open(export_data, 'w') as export_data:
        export_data.write(str_data_for_export)
    return str_data_for_export

def search_contact_in_data_base(db: list[str]):
    contact = input('Напишите имя контакта => ')
    for i in range(len(db)):
        for j in range(len(db[i])):
            if contact.lower() in db[i][j].lower():
                return print('Контакт который вы искали => ', db[i])
            else:
                return print('\nКонтакта нет в базе\n')

def print_data_base():
    data = []
    split_data = read_data_base().split('\n\n')
    for i in split_data:
        data.append(i.split('\n'))
    return data 

def delete_contact_from_data_base(list_data_base: list[str]):
    contact = input('Напините имя контакта, который необходимо удалить => ')
    dict_for_search = {}
    for i in range(len(list_data_base)):
        if contact in list_data_base[i]:
            dict_for_search = list_data_base[i]
    print(dict_for_search)
    while(key_:= int(input('Выберете номер контакта, который необходимо удалить => '))) not in dict_for_search:
        print('Некорктный ввод!')
    else:
        list_data_base.remove(dict_for_search[key_])
    return list_data_base
# print(delete_contact_from_data_base(read_data_base()))
