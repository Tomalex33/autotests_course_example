# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

s = all_division(20, 2)
print(s)


@pytest.mark.parametrize('a, b, res', [(2, 2, 1), (4, 2, 2), (2, 0, 0)], ids=['positive ', 'positive ', 'negative '])
@pytest.mark.smoke
def test_del_0(a, b, res):
    assert all_division(a, b) == res, "Деление на ноль"
    print("ошибка")

@pytest.mark.smoke
def test_positiv():
    assert all_division(200, 2) == 100.0

def test_del_1():
    assert all_division(200, -1) == -200

def test_bigpositiv():
    assert all_division(200000, 25) == 8000
