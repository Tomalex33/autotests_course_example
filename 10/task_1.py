# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random

letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def generate_random_name():
    si = ''
    k = random.randint(1, 15)
    b = random.sample(letter_list, k)
    for i in b:
        si = si + i
    si1 = ''
    k1 = random.randint(1, 15)
    b1 = random.sample(letter_list, k1)
    for u in b1:
        si1 = si1 + u

    return f'{si} {si1}'

print(generate_random_name())


