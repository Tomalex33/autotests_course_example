# my_list = []
# for i in range(1, 6):
#     if i % 2 == 0:
#         my_list.append(i)
# print(my_list)
#
# my_list1 = [i for i in range(1, 6) if i % 2 == 0]
# print(my_list1)

# my_age = 18
# if my_age <= 18:
#     res = my_age + 1
#     print(res)
# elif my_age >= 19:
#     res = my_age - 1
#     print(res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     elif i == 2:
#         continue
#     i += 1
#     print(i)

# a = 2
# b = 3
# c = 4
#
# if a + b <= c or a + c <= b or b + c <= a:
#     print('Не треугольник')
# elif a == b == c:
#     print('Равносторонний')
# elif b == c or a == c or a == b:
#     print('Равнобедренный')
# elif (a ** 2) + (b ** 2) == c ** 2:
#     print('Обычный')
# else:
#     print('Другой треугольник')

# num = 996
# digits = []
# delet = [num % 10] + digits
# dele = num // 10
# print(f'{delet}')
# print(dele)

# def degits_iter(num):
#     digits = []
#     while num:
#         digits = digits + [num % 10]
#         print(digits)
#         num = num // 10
#         print(num)
#     return digits[::-1] or [0]
# print(degits_iter(996))
#
# a = [3]
# b = 2
# multy = a * b
# print(multy)

# num = 0
# while num < 3:
#     num = num + 1
#     print(num)

# num = 10
# digits = 1
# count_multy = 0
# while count_multy < 20:
#     if num <= 9:
#         print(count_multy)
#     elif num >= 10:
#         count_multy = count_multy + 1
#         print(count_multy)

# while num:
#     digits = digits * (num % 10)
#     num = num // 10
#     count_multy = count_multy + 1
# print(digits)
# print(count_multy)

num = 10
count = 0
digits = 1
if num < 10:
    print(count)
else:
    while num:
        digits = digits * (num % 10)
        num = num // 10
        print(digits)
