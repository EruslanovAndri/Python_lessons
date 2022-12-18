contact_data_base = r'/Users/eruslanovandrey/Python_lessons/Home_Work_Lesson_7/Contact_file.txt'


def create_new_contact():  # Добавляет новый контакт в фаил
    with open(contact_data_base, 'r+') as data:
        if data.read() == '':
            data.write(input('Write name => ')+'\n')
            data.write(input('Write surname => ')+'\n')
            data.write(input('Write telephone => '))
        else:
            data.write('\n\n'+input('Write name => ')+'\n')
            data.write(input('Write surname => ')+'\n')
            data.write(input('Write telephone => '))


def read_data():  # Читает фаил
    with open(contact_data_base, 'r') as data:
        return data.read()


def rewrite_data_base(data: list):  # Перезаписывает БД после удаления контакта
    with open(contact_data_base, 'w') as data:
        data.write(data)
