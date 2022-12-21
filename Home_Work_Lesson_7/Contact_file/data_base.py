contact_data_base = r'/Users/eruslanovandrey/Python_lessons/Home_Work_Lesson_7/Contact_file.txt'


def create_new_contact():  # Добавляет новый контакт в фаил
    with open(contact_data_base, 'r+') as data:
        name = input('Enter a name => ')
        surname = input('Enter a surname => ')
        telephone = input('Enter a telephone number =>  ')
        if data.read() == '':
            data.write(f'{name}\n{surname}\n{telephone}')
        else:
            data.write(f'\n\n{name}\n{surname}\n{telephone}')

def read_data():  # Читает фаил
    with open(contact_data_base, 'r') as data:
        return data.read()

def print_pretty_tables():
    my_list = my_string_To_list()
    mytable = PrettyTable(['Name', 'Surname', 'Telephone'])
    for i in range(len(my_list)):
        ','.join(my_list[i])
        mytable.add_row(my_list[i])
    mytable.add_autoindex('ID')
    print(mytable)
print_pretty_tables()


def rewrite_data_base(data: list):  # Перезаписывает БД после удаления контакта
    with open(contact_data_base, 'w') as data:
        data.write(data)
