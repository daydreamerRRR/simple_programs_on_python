import random
from random import *

import colorama
from colorama import Fore
colorama.init()

def count_of_guessed(count_of_guessed_temp):
    if count_of_guessed_temp % 10 == 1 and (count_of_guessed_temp % 100 < 5 or count_of_guessed_temp % 100 > 20):
        print(f'Вы правильно высчитали {count_of_guessed_temp} число!')
    elif 2 <= count_of_guessed_temp % 10 <= 4 and (count_of_guessed_temp % 100 < 5 or count_of_guessed_temp % 100 > 20):
        print(f'Вы правильно высчитали {count_of_guessed_temp} числа!')
    else:
        print(f'Вы правильно высчитали {count_of_guessed_temp} чисел!')

def fool_check(user_command_temp, values):
    while user_command_temp.lower() not in values:
        print('Некорректный ввод. Введите ', end='')
        if len(values) == 1:
            print(f'«{values[0]}».')
        for i in range(len(values) - 1):
            if i == len(values) - 2:
                print(f'«{values[i]}» или «{values[i + 1]}».')
            else:
                print(f'«{values[i]}», ', end='')
        user_command_temp = input()
    return user_command_temp.lower()

def digit_check(user_command_temp):
    while not user_command_temp.isdigit() or int(user_command_temp) <= 0:
        print('Некорректный ввод. Введите число больше 0.')
        user_command_temp = input()
    user_command_temp = int(user_command_temp)
    return user_command_temp

print("Привет!")
print('Это программа-тренировка для быстрого перевода чисел из 2, 8 и 16 систем счисления в 10')
user_command = fool_check(input('Начать тренировку? да/нет\n'), ['да', 'нет'])
if user_command == 'да':
    print('Введите систему счисления для тренировки (2, 8, 16, rand):')
    numeral_system = fool_check(input(), ['2', '8', '16', 'rand'])
    print('Введите диапазон чисел для перевода в выбранную систему счисления:')
    print('«1». от 10 до 100 (не включительно)')
    print('«2». от 100 до 1000 (не включительно)')
    diapason = int(fool_check(input(), ['1', '2']))
    guessed_counter = 0
    while user_command == 'да':
        numeral_temp = numeral_system
        guessing_num = randint(10**diapason, 10**(diapason+1))
        if numeral_system == 'rand':
            numeral_system = choice(['2', '8', '16'])
        if numeral_system == '2':
            print(bin(guessing_num)[2:] + '₂')
        elif numeral_system == '8':
            print(oct(guessing_num)[2:] + '₈')
        elif numeral_system == '16':
            print(hex(guessing_num)[2:].upper() + '₁₆')
        numeral_system = numeral_temp
        print('Введите ответ:')
        user_command = digit_check(input())
        if user_command == guessing_num:
            print(Fore.GREEN + 'Верно!' + Fore.RESET)
            guessed_counter += 1
        else:
            print(Fore.RED + 'Неверно!' + Fore.RESET)
            print(Fore.LIGHTBLUE_EX + 'Правильный ответ ' + Fore.RESET + '— '+ str(guessing_num))
        count_of_guessed(guessed_counter)
        print('Хотите сыграть ещё один раунд?')
        user_command = fool_check(input(), ['да', 'нет'])
print('До встречи!')
input()
'''
Описание работы программы:
1. Пользователю предлагается выбрать основание системы счисления,
   из которой нужно будет число в десятичную.
2. Пользователь выбирает диапазон, в котором числа из десятичной системы
   будут переходить в n-ую. На выбор:
   2.1. от 10 до 100 (включительно)
   2.2. от 100 до 1000 (включительно)
3. Пользователь вводит количество чисел, которые нужно перевести из одной системы в другую.
   Количество чисел может быть только натуральным числом.
4. Программа берёт случайное число из заданного в шаге (2) диапазона,
   затем переводит его в 2, 8 или 16-и ричную систему при помощи функции bin() (см. #TODO),
   записывая результат в отдельную переменную.
5. Начинается игра. К полученному в шаге (4) числу приписывается маленький символ системы снизу (см. #TODO).
6. Пользователь вводит число в десятичной системе.
   6.1. Если число, которое ввёл пользователь, совпадает с тем, которое было «загадано»,
   программа выводит поздравительное сообщение.
   6.2. Если число, которое ввёл пользователь, не совпадает с тем, которое было «загадано»,
   программа выводит сообщение о том, что пользователь ошибся.
7. Повторять шаг (4), пока количество раундов не будет равно количеству чисел,
   полученных в шаге (3).
   
ИДЕИ ПО УЛУЧШЕНИЮ ПРОЕКТА:
 - ✔ Сделать перевод разных чисел из заданного диапазона в случайную (2, 8, 16) систему счисления.
 - Добавить счётчик очков. В зависимости от того, что выбрал пользователь в шаге (1),
   за правильное «угадывание» выдаётся разное количество очков:
   - из 2 в 10 -- 10 очков
   - из 8 в 10 -- 20 очков
   - из 16 в 10 -- 50 очков
   - в случае ошибки у пользователя отнимается 30 очков.
'''