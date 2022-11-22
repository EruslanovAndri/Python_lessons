# Task_5 Напишите пр-му, которая принимает на вход число о проверяет,
# кратно ли оно на 5 и на 10 или 15, но не 30.
n = int(input('Enter a number = '))
if (((n % 5 == 0) and (n % 10 == 0)) or (n % 15 == 0)) and (n % 30 != 0):
    print(True)
else:
    print(False)    
