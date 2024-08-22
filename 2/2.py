# Первое задание.

# from math import sqrt
# a = 4                                            # Значение стороны квадрата
# perimeter_square = a * 4                         # Значение периметра квадрата
# area_square = a * a                              # Значение площади квадрата
# diagonal_square = sqrt((a**2)+(a**2))            # Значение диагонали квадрата
#
# print(f'Периметр квадрата = {perimeter_square}')
# print(f'Площадь квадрата = {area_square}')
# print(f'Диагональ квадрата = {diagonal_square}')

# Второе задание.

# a = 1
# b = 12
# c = 9
#
# D = (b ** 2) - (4 * a * c)
# x1 = (-b + sqrt(D)) / 2 * a
# x2 = (-b - sqrt(D)) / 2 * a
# print(D)
# print(round(x1, 2))
# print(round(x2, 2))

# Третье задание.

# text1 = 'Привед '
# text2 = 'Медвед'
# a = text1[0:2]
# b = text2[0:2]
# c = text1[2:]
# d = text2[2:]
# total = b + c + a + d
# print(total)

# Четвертое задание.

path = r'C:\Users\ap.tomchik\Downloads\todolist.txt'
print(path[path.rfind('\\') + 1:path.rfind('.')])

# Пятое задание.

# a = 5
# b = 10
# c = a + b
# print(f'{a} + {b} = {c}')
#
# a = 4
# b = 2
# c = a * b
# print(f'{a} * {b} = {c}')

# Шестое задание.

# text = 'Привед медвед?'
# result = ''
# for i in range(len(text)):
#     if i % 2 < 1 and i != 0:
#         result += text[i]
#
# print(result)

# Седьмое задание.

# first_string = 'tgh'
# second_string = 'qfertyuiopasdwghjklzxcvbnm'
#
# first_letter = second_string.find(first_string[0])
# second_letter = second_string.find(first_string[1])
# third_letter = second_string.find(first_string[2])
#
# start = min(first_letter, second_letter, third_letter)
# end = max(first_letter, second_letter, third_letter)
#
# print(second_string[start:end+1])
