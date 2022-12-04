f_path = r'my_file.txt'
with open(f_path,'w') as data:
    my_num = input('Enter a number:')
    data.write(f'{my_num}\n')

with open(f_path,'r') as data:
    read_data = data.read()
split_data = read_data.split(' ')
convert_data_int = [int(i) for i in split_data]
max_num = max(convert_data_int)
min_num = min(convert_data_int)

with open(f_path,'a') as data:
    data.write(f'max = {max_num}\n')
    data.write(f'min = {min_num}\n')