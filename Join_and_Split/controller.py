from funcs import read_data_base,my_list_To_string,my_string_To_list,print_data_base,export_data_base_txt_format,export_data_base_csv_format,search_contact_in_data_base,sort_data,print_pretty_tables
from data_base import *

def button_click():
    while True:
        print('Напишите вариант 1 или 2 в зависимости от необхидимого результата.')
        print('Вариант номер 1 - Преобразовывает список со строками в строку.')
        print('Вариант номер 2 - Преобразовывает строку в список строк.')
        print('Вариант номер 3 - Добавить новую информацию в базу данных.')
        print('Вариант номер 4 - Принт базу данных в терминал.')
        print('Вариант номер 5 - Экспорт базы данных в фаил в формате .txt.')
        print('Вариант номер 6 - Экспорт базы данных в фаил в формате .scv.')
        print('Вариант номер 7 - Поиск контакта.')
        print('Вариант номер 8 - Удаление контактов.')
        print('Вариант номер 9 - Вывод контактов.')
        print('Вариант номер 10 - Вывод контактов в таблицу.')
        print('Вариант номер 11 - Выход.')
        choice = int(input('Напишите ваш вариант => '))
        if choice ==  1:
            print(my_list_To_string(read_data_base())) # В качестве аргумента должна приходить информация из БД
        elif choice == 2:
            print(my_string_To_list())
        elif choice == 3:
           add_information_in_data_base()
        elif choice == 4:
            print(sort_data(print_data_base()))
        elif choice == 5:
            export_data_base_txt_format(my_list_To_string(read_data_base()))
        elif choice == 6:
            export_data_base_csv_format(my_list_To_string(read_data_base()))
        elif choice == 7:
            print(search_contact_in_data_base(print_data_base()))
        elif choice == 8:
            print(delete_contact_from_data_base(print_data_base())) # DONT WORK
        elif choice == 9:
            conclusion_contact()
        elif choice == 10:
           print_pretty_tables()
        elif choice == 11:
            break


    


