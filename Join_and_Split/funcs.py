from pathlib import Path
from data_base import *
from prettytable import PrettyTable


def my_list_To_string(db: list[str]): #WORK
    for i in range(len(db)):
        for j in range(len(db[i])):
            my_string = ''.join(db)
    return my_string


def my_string_To_list():  # WORK
    my_list = []
    temp_list = read_data_base().split('\n\n')
    for i in temp_list:
        my_list.append(i.split('\n'))
    # print(f'List = ',my_list)
    return my_list


def export_data_base_txt_format(db: list[str]): # WORK
    str_data_for_export = my_list_To_string(db)
    export_data = Path('export_data.txt')
    with open(export_data, 'w') as export_data:
        export_data.write(str_data_for_export)
    return str_data_for_export

def export_data_base_csv_format(db: list[str]): # WORK
    str_data_for_export = my_list_To_string(db)
    export_data = Path('export_data.scv')
    with open(export_data, 'w') as export_data:
        export_data.write(str_data_for_export)
    return str_data_for_export

def search_contact_in_data_base(db: list[str]): # WORK
    contact = input('Напишите имя контакта => ')
    for i in range(len(db)):
        for j in range(len(db[i])):
            if contact.lower() in db[i][j].lower():
                return print('Контакт который вы искали => ', db[i])
    else:
        return print(f'\nКонтакта <<{contact}>> нет в базе\n')

def print_data_base(): # WORK
    data = []
    split_data = read_data_base().split('\n\n')
    for i in split_data:
        data.append(i.split('\n'))
    return data 

def sort_data(db): # WORK
    data_list = []
    for i in range(len(db)):
        data_list.append(db[i])
        data_list.sort()
    return(data_list)


def print_pretty_tables():
    my_list = my_string_To_list()
    mytable = PrettyTable(['Name', 'Surname', 'Telephone'])
    for i in range(len(my_list)):
        ','.join(my_list[i])
        mytable.add_row(my_list[i])
    mytable.add_autoindex('ID')
    print(mytable)

def delete_contact_from_data_base(list_data_base: list[str]): # DON'T WORK
    contact = input('Напините имя контакта, который необходимо удалить => ').lower()
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
