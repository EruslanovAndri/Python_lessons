from pathlib import Path
from data_base import *
from prettytable import PrettyTable
# from logger import logger_
from funcs import *


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

def search_contact_in_data_base(db: list, find_contact: str): # WORK
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


def print_pretty_tables(): # Work
    my_list = sort_data(my_string_To_list())
    mytable = PrettyTable(['Name', 'Surname', 'Telephone'])
    for i in range(len(my_list)):
        ','.join(my_list[i])
        mytable.add_row(my_list[i])
    mytable.add_autoindex('ID')
    print(mytable)

# def delete_contact_from_data_base(db: str):
#     contact = search_contact_in_data_base(my_string_To_list(),db)
#     data_list = my_string_To_list()
#     if len(contact) != 0:
#         while (key_:= int(input('Enter a number of contact for datele => '))) not in contact:
#             print('There is no such contact in the book. Try one more time => ')
#         else:
#             # logger_(''.join(data_list[key_]))
#             data_list.remove(contact[key_])
#     return data_list

# print(delete_contact_from_data_base(read_data_base()))

