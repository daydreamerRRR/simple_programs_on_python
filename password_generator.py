from random import *


# проверка, ввёл ли пользователь корректные числовые данные в тех местах, в которых это требуется (кол-во паролей и длина каждого).
def is_idiot_nums(n):
    if not n.strip().isdigit():
        print('Неккоректные данные.')
        return True


# проверка, включать ли символы определённого типа, будь то цифры, прописные/строчные буквы и тд., в пароль.
def is_include(n, s):
    while True: 
        if n not in ('да', 'нет'):
            print('Неккоректные данные.')
            n = input(f'Включать ли {s} в пароль? (да/нет)\n') 
            continue
        if n.strip() == 'да':
            return True
        elif n.strip() == 'нет':
            return False
		
		
# проверка, подходит ли пароль по всем критериям.
# если нет, генерируется заново.		
def is_valid_password(psw, flg_list):
    is_ok = True
    if flg_list[0]:
        if flg_list[1] or flg_list[2]:
            is_ok = psw.isalnum()
        else:
            is_ok = psw.isdigit()
    return is_ok


def main():
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chars = ''
    password = ''
    count = input('Сколько паролей сгенерировать?\n')
    while is_idiot_nums(count):
        count = input('Сколько паролей сгенерировать?\n')
    count = int(count)
    i = 0
    while i != count:
        i += 1
        length = input(f'Какова длина {i} пароля?\n')
        while is_idiot_nums(length):
            length = input(f'Какова длина {i} пароля?\n')
        length = int(length)
        string = ['цифры', 'прописные буквы', 'строчные буквы', 'неоднозначные символы (il1Lo0O)']
        flags = [is_include(input(f'Включать ли {string[i]} в пароль? (да/нет)\n'), string[i]) for i in range(4)]
        if flags[0]:
            chars += digits
        if flags[1]:
            chars += uppercase_letters
        if flags[2]:
            chars += lowercase_letters
        if not flags[3]:
            for c in 'il1Lo0O':
                chars = chars.replace(c, '')
        if not flags[0] and not flags[1] and not flags[2] and not flags[3] or len(chars) < length:
            print('Неккоректные данные.')
            i -= 1
            continue
        password = ''.join(sample(chars, length))
        while not is_valid_password(password, flags):
            password = ''.join(sample(chars, length))
        print(*password, sep='')
    input('Нажмите любую клавишу для выхода из программы')

if __name__ == '__main__':
	main()
