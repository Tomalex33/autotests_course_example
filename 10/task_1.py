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

# import random
#
# letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# def generate_random_name():
#     word = ''
#     for i in letter_list:
#         yield random.choice(letter_list) + word
#         print(word, 'добавляем букву')
#         word = word + i
#
# gen = generate_random_name()
#
# for p in gen:
#     print(p)

# new_word = ''
# s = random.choice(letter_list)
# new_word = new_word + s
# print(new_word)

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def my_range(start, end=None):
#     if end is None:
#         start, end = 0, start
#         yield start
#         start = start + 1
#         if start == end:
#             raise StopIteration("end")
#
#
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in random.choice(letter_list):
    print(i)
#     s = random.choice(letter_list)
# print(s)