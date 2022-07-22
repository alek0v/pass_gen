from random import choice

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
bloknot = ''

def guest_prov(q):
    while True:
        if q.lower() == "д" or q.lower() == "да":
            return True
        elif q.lower() == 'н' or q.lower() == 'нет':
            return False
        else:
            q = input('Некорректный ответ, введите д (да) или н (нет): ')

def num_prov(num):
    while True:
        if not num.isdigit():
            num = input('Некорректные данные. Введите целое, положительное число: ')
            continue
        elif int(num) > 0:
            break
        elif int(num) <= 0:
            num = input('Некорректные данные. Введите целое, положительное число: ')
    return int(num)

def gen_pass(bloknot, lenn):
    out = ''
    for i in range(lenn):
        out += choice(bloknot)
    return out

print("\nВас приветствует генератор паролей. Для быстроты ответа на вопросы вводите д (да), н (нет).")
amount = num_prov(input("Сколько паролей вам нужно сгенерировать? "))
lengs = num_prov(input('Какая должна быть длинна пароля? '))

if guest_prov(input('Сделать пароль сложным? ')):
    bloknot += digits + lowercase_letters + uppercase_letters + punctuation
else:
    if guest_prov(input('Включать ли цифры 0123456789? ')):
        bloknot += digits
    if guest_prov(input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ')):
        bloknot += lowercase_letters
    if guest_prov(input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ')):
        bloknot += lowercase_letters
    if guest_prov(input('Включать ли символы !#$%&*+-=?@^_? ')):
        bloknot += punctuation
    if guest_prov(input('Хотите ли вы исключить какие то символы? д (да) или н (нет) ')):
        q = input('Какие символы вы хотите исключить? (Переличите их без пробелов и запятых) ')
        for i in q:
            if i in bloknot:
                bloknot = bloknot[:bloknot.find(i)] + bloknot[bloknot.find(i) + 1:]

print()
for i in range(amount):
    print(i + 1, "пароль: ", gen_pass(bloknot, lengs))

input("\nНажмите 'Enter' для закрытия программы ")