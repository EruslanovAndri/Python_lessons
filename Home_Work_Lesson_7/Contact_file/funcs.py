from data_base import read_data
import csv
from pathlib import Path

def print_all_data(): # Печатает всю базу данных
    data_split = []
    s = read_data().split('\n\n')
    for i in s:
        data_split.append(i.split('\n'))
    return data_split 

# print(print_all_data())

def search_contact(data_split):  # Ищет конкретный контакт в БД
    search = input('Write the name of searching contact => ')
    for i in range(len(data_split)):
        for j in range(len(data_split[i])):
            if search.lower() in data_split[i][j].lower():
                return data_split[i]

# print(search_contact(print_all_data()))

def delete_contact(data_list: list): # Находить контакт который нужно удалить
    want_deleted = input('Write the contact are you want to be deleted => ')
    new_data_base_after_deletion = {}
    for i in range(len(data_list)):
        if want_deleted in data_list[i]:
            new_data_base_after_deletion[i] = data_list[i]
    print(new_data_base_after_deletion)
    while (key_:=int(input('Enter a number of contact for delete => '))) not in new_data_base_after_deletion:
        print('Wrong number.')
    else:
        data_list.remove(new_data_base_after_deletion[key_])
    return data_list

# print(delete_contact(print_all_data()))

def data_to_string(data: list):
    tempt_list = []
    for i in range(len(data)):
        tempt_list.append('\n'.join(data[i]))
    temp_str = '\n\n'.join(tempt_list)
    return temp_str

def sort_data(data: list):
    data.sort()
    return data

