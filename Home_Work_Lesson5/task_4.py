# Task 4. Реализуйте RLE алгоритм: реализуйте модуль 
# сжатия и восстановления данных.

# Входные и выходные данные хранятся в 
# отдельных текстовых файлах.
text = ''
def print_my_message(text):
    text = str(input('Enter the message: => '))
    return text

def encode_text(text):
    count = 1
    res = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            res = res + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        res = res + str(count) + text[-1]
    return res

def decoded_text(text):
    num = ''
    res = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            num += text[i]
        else:
            res = res + text[i] * int(num)
            num = ''
    return res

with open('text.txt','w') as data:
    data.write(encode_text(print_my_message(text)))


with open('text.txt','r') as data:
    data.read(decoded_text(text))
    
print(encode_text(print_my_message(text)))
print(decoded_text(print_my_message(text)))



