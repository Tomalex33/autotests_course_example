# Напишите функцию multiplication_chain, которая принимает положительное число num,
# и возвращает количество раз count_multy, которое вы должны перемножить цифры числа num и полученных произведений,
# пока не получите одну цифру.
# Например (Ввод --> Вывод) :
#
# 39 --> 3 (потому что 3*9 = 27, 2*7 = 14, 1*4 = 4, вот 4 одна цифра. Итого 3 итерации)
# 999 --> 4 (потому что 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, наконец 1*2 = 2, Итого 4 итерации)
# 4 --> 0 (4 уже одна цифра, а значит мы проделали 0 итераций)

def multiplication_chain(num):
    def degits_iter(num):
        digits = 1
        count_multy = 0
        if num >= 10:
            count = 0
        while digits >= 10:
            digits = digits * (num % 10)
            num = num // 10
            count = count + 1
        return count
    count_multy = count_multy + 1
    return count_multy
print(multiplication_chain(25))

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    39, 4, 25, 999, 5050, 222333444
]

test_data = [
    3, 0, 2, 4, 1, 4
]


for i, d in enumerate(data):
    assert multiplication_chain(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')


num = 39
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