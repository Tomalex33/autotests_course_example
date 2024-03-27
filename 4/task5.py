
# Задача Иосифа Флавия
# https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D0%98%D0%BE%D1%81%D0%B8%D1%84%D0%B0_%D0%A4%D0%BB%D0%B0%D0%B2%D0%B8%D1%8F
# Задача заключается в следующем: по кругу стоит num_people воинов,
# начиная с первого воина они выводят из круга каждого kill_num по счёту.
# Вы должны правильно указать, кто является «выжившим», то есть: последний элемент списка.
#
# num_people=7, kill_num=3 => Значит 7 человек в кругу и каждый третий из него выходит
# [1,2,3,4,5,6,7] - начальный круг
# [1,2,4,5,6,7] => 3 вышел
# [1,2,4,5,7] => 6 вышел
# [1,4,5,7] => 2 вышел
# [1,4,5] => 7 вышел
# [1,4] => 5 вышел
# [4] => 1 вышел, 4 остался последним т.е. выжившим - это наш ответ survivor.
def do_list(num_people):
    L = []
    while num_people > 0:
        L.append(num_people)
        L.sort()
        num_people = num_people - 1
    return L
def josephus_task(num_people, kill_num):
    s = do_list(num_people)
    ind = kill_num - 1
    while len(s) > 1:
        if ind < len(s) - 1 and ind != 0:
            s.pop(ind)
            ind = ind + 2
            print(ind, 'ind первое условие')
        elif ind == 0:
            ind = -1
            s.pop(ind)
            print(ind, 'ind второе условие')
        else:
            print('попал в else')
            ind = (ind - len(s)) - 1
            s.pop(ind)
            print(ind, 'ind третье условие')
        print(s, 'это s')
    survivor = s.pop(0)
    return survivor

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    (7, 3), (11, 19), (1, 300), (14, 2), (100, 1), (1234, 56), (987, 11)
]

test_data = [
    4, 10, 1, 13, 100, 1130, 379
]


for i, d in enumerate(data):
    assert josephus_task(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
