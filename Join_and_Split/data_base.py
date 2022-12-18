from pathlib import Path
def add_information_in_data_base():
    db = Path('my_data_base.txt')
    with open(db, 'a', encoding='UTF-8') as data:
        if data == '':
            data.write(input('Add new information in the data base => ')+'\n')
        else:
            data.write(
                input('\n' + 'Add new information in the data base => ')+'\n\n')

def read_data_base():
    db = Path('my_data_base.txt')
    with open(db, 'r', encoding='UTF-8') as data:
        return data.read()


