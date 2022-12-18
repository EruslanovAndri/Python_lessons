from data_base import create_new_contact,rewrite_data_base,read_data
from funcs import print_all_data,delete_contact,search_contact,data_to_string,sort_data

def choose_the_option():
    while True:
        print('\n Enter the number of the option from 1 to 5 wich are you going to use: ')
        print(' 1 -Create new contact.\n',#WORK
                '2 - Delete contact.\n',#WORK
                '3 - Search contact.\n',#WORK
                '4 - Print all data.\n'#WORK
                '7 - *****Exit\n')#WORK
        option = input('=> ')
        print('')
        if option == '1':
            create_new_contact()
            return choose_the_option()
        elif option == '2':
            rewrite_data_base(delete_contact(data_to_string()))
        elif option == '3':
            print(f'Contact was found =>{search_contact(print_all_data())}')
        elif option == '4':
            print(sort_data(print_all_data()))
        elif option == '7':
            break
choose_the_option()
