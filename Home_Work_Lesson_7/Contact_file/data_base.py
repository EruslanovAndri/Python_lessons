contact_data_base = r'/Users/eruslanovandrey/Python_lessons/Home_Work_Lesson_7/Contact_file.txt'

def create_new_contact(): # Добавляет новый контакт в фаил
    with open(contact_data_base,'a') as data:
        data.write(input('Write name => ')+'\n')
        data.write(input('Write surname => ')+'\n')
        data.write(input('Write telephone => ')+'\n\n')
        
def read_data(): # Читает фаил
    with open(contact_data_base,'r') as data:
        return data.read()

def rewrite_data_base(data:list): # Перезаписывает БД после удаления контакта
    temp_data = []
    for i in range(len(data)):
        temp_data.append('\n'.join(data[i]))
    temp_str = '\n\n'.join(temp_data)
    with open(contact_data_base,'w') as data:
        data.write(temp_str)


