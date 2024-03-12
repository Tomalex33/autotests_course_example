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

a = 2
b = 3
c = 4

if a + b <= c or a + c <= b or b + c <= a:
    print('Не треугольник')
elif a == b == c:
    print('Равносторонний')
elif b == c or a == c or a == b:
    print('Равнобедренный')
elif (a ** 2) + (b ** 2) == c ** 2:
    print('Обычный')
else:
    print('Другой треугольник')
