# Task 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""
import random
sweets = 2021
take = 0
how_start = random.randint(1, 2)
if how_start == 1:
    print('Начинает первый игрок')
else:
    print('Начинает второй игрок')
print()
while sweets >= 1:
    if how_start == 1:
        print('Ход первого игрока: ')
        print()
        take = int(input('Возьмите конфеты со стола от 1 до 28 => '))
        if take <= 28:
            balance = sweets - take
            sweets -= take
            print()
            print(f'На столе осталось', balance, 'конфет.')
            print()
            how_start = 2   
            if balance <= 1:
                print('Второй игрок победил.')
                break
        else:
            print()
            print('Вы взяли слишком много конфет, попробуйте еще раз.')
            print()
            sweets += take - take
            how_start == 1

    if how_start == 2:
        print('Ход вторго игрока: ')
        print()
        take = random.randint(1,28) # Bot 
        print(f'Bot took = ',take)
        # take = int(input('Возьмите конфеты со стола от 1 до 28 => ')) # Игрок номер 2 вводит самостоятельно значение.
        if take <= 28:
            balance = sweets - take
            sweets -= take
            print()
            print(f'На столе осталось', balance, 'конфет.')
            print()
            how_start = 1
            # if balance < 100 and balance % 29 == 0:
            #     take = balance 
            if balance <= 1:
                print('Первый игрок победил.')
                break

        else:
            print()
            print('Вы взяли слишком много конфет, попробуйте еще раз.')
            print()
            sweets += take - take
            how_start == 2


   
        
    
      
