from pathlib import Path
def add_information_in_data_base():
    db = Path('my_data_base.txt')
    with open(db, 'r+', encoding='UTF-8') as data:
        name = input('Enter a name => ')
        surname = input('Enter a surname => ')
        telephone = input('Enter a telephone number =>  ')
        if data.read() == '':
            data.write(f'{name}\n{surname}\n{telephone}')
        else:
            data.write(f'\n\n{name}\n{surname}\n{telephone}')
        

def read_data_base():
    db = Path('my_data_base.txt')
    with open(db, 'r', encoding='UTF-8') as data:
        return data.read()


def conclusion_contact():
    db = Path('my_data_base.txt')
    with open(db, 'r',encoding='UTF-8') as data:
        print('=====================')
        return print(data.read())
        