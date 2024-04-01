import math
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

# while num:
#     digits = digits * (num % 10)
#     num = num // 10
#     count_multy = count_multy + 1
# print(digits)
# print(count_multy)

# num = 996
# count = 0
# digits = 1
# if num < 10:
#     print(count)
# else:
#     while digits < 10:
#         digits = digits * (num % 10)
#         num = num // 10
#         print(digits)
#         print(num)

# def degits_iter(num):
#     digits = []
#     while num:
#         digits = digits + [num % 10]
#         num = num // 10
#     return digits[::-1] or [0]
# prod = [9, 9, 6]
# print(math.degits_iter(996))
# print(math.prod([9, 9, 6]))

# num = 996
# while mylty >= 10:
#     mylty = eval(str(degits_iter(num))[1:-1].replace(',', '*'))
#     print(mylty)
#     def degits_iter(num):
#      digits = []
#      while num:
#         digits = digits + [num % 10]
#         num = num // 10
#         return digits[::-1] or [0]
#     print(degits_iter(num))
#
# print(mylty)

# num = 39
# count = 0
# def degits_iter(num):
#     digits = []
#     while num:
#         digits = digits + [num % 10]
#         num = num // 10
#     return digits[::-1] or [0]
#
# if num < 10:
#    print('1 итерация')
# else:
#     print('Итераций больше, нужно посчитать')
#     sum_mylty = eval(str(degits_iter(num))[1:-1].replace(',', '*'))
#     print(sum_mylty) ## 27
#     new_number = degits_iter(sum_mylty)
#     print(degits_iter(sum_mylty)) ## [2, 7]
#     sum_mylty = eval(str(degits_iter(new_number))[1:-1].replace(',', '*'))
#     print(sum_mylty)


# num = 155
# digits = 1
# count = 0
# while digits:
#     digits = digits * (num % 10)
#     print(digits)
#     num = num // 10
#     print(num)
#     count = count + 1
# print(count)

# "(123) 456-7890"
# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# print(f'({a[0]}'+f'{a[1]}'+f'{a[2]}) '+f'{a[3]}'+f'{a[4]}'+f'{a[5]}-'+f'{a[6]}'+f'{a[7]}'+f'{a[8]}'+f'{a[9]}')

# L = [1, 0, 1, 2, 0, 1, 3]
# R = []
# Res = []
# for num in L:
#     if num == 0:
#         print(num, 'Первый случай')
#         R.append(num)
#     else:
#         print(num, 'Второй случай')
#         Res.append(num)
# print(R)
# print(Res)
# print(Res+R)

