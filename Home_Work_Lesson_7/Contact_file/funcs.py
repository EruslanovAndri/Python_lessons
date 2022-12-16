from data_base import read_data,rewrite_data_base

def print_all_data(): # Печатает всю базу данных
    data_split = []
    s = read_data().split('\n\n')
    for i in s:
        data_split.append(i.split('\n'))
    return data_split 

def search_contact(data_split):  # Ищет конкретный контакт в БД
    search = input('Write the name of searching contact => ')
    for i in range(len(data_split)):
        for j in range(len(data_split[i])):
            if search.lower() in data_split[i][j].lower():
                return data_split[i]

def delete_contact(data_split): # Находить контакт который нужно удалить
    want_deleted = input('Write the contact are you want to be deleted => ')
    new_data_base_after_deletion = []
    for i in range(len(data_split)):
        if want_deleted in data_split[i]:
            new_data_base_after_deletion.append(data_split[i])
    return new_data_base_after_deletion


