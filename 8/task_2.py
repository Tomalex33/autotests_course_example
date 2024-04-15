# Напишите класс Trigon, для инициализации передаётся неизвестное кол-во атрибутов

# В классе при инициализации происходит проверка на корректность переданных данных и генерируются следующие исключения:

# 1) Если хотя бы одна сторона передана не числом,
# то падаем с TypeError и текстом 'Стороны должны быть числами'

# 2) Если хотя бы одна сторона передана нулем или отрицательным числом,
# то падаем с ValueError и текстом 'Стороны должны быть положительными'

# 3) Если не соблюдается неравество треугольника,
# то Exception и текст "Не треугольник"

# 4) Если передано не 3 аргумента, то IndexError "Передано {n} аргументов, а ожидается 3", где n - кол-во аргументов

import unittest  # Не удалять

class Trigon:
    def __init__(self, *args):
        self.args = args

    def date_type(self):
        try:
            for i in self.args:
                if type(i) != int:
                    7 + 'd'  # если данные не int создаем исключение
        except TypeError:
            return 'Стороны должны быть числами'
        else:
            return 'Все данные int'

    def date_value(self):
        try:
            for i in self.args:
                if i <= 0:
                    (int('Data'))
        except ValueError:
            return 'Стороны должны быть положительными'
        else:
            return 'Все cтороны положительные'

    def trigon_true(self):
        try:
            if self.args[0] >= self.args[1] + self.args[2]:
                6/0
            elif self.args[1] >= self.args[2] + self.args[0]:
                6/0
            elif self.args[2] >= self.args[1] + self.args[0]:
                6/0
        except Exception:
            return "Не треугольник"
        else:
            return 'Треугольник можно построить с переданными значениями'

    def trigon_arg(self):
        n = 0
        for i in self.args:
            n = n + 1
        try:
            if n != 3:
                print(self.args[-55551])
        except IndexError:
            return f'Передано {n} аргументов, а ожидается 3'
        else:
            return "Всё хорошо, передано правильное количество сторон для треугольника"

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


class MyTestCase(unittest.TestCase):

    def test(self):
        data = [(3, '7', 5), (-3, 7, 5), (2, 5, 2), (3, 4, 5, 6), (3, 4), (3, 4, 5)]

        test_data = [('Стороны должны быть числами', 'TypeError'),
                     ('Стороны должны быть положительными', 'ValueError'),
                     ("Не треугольник", 'Exception'),
                     ("Передано 4 аргументов, а ожидается 3", 'IndexError'),
                     ("Передано 2 аргументов, а ожидается 3", 'IndexError'),
                     0]
        for i, d in enumerate(data):
            try:
                Trigon(*data[i])
            except Exception as e:
                assert e.args[0] == test_data[i][0], 'Исключение имеет неправильный текст'
                assert type(e).__name__ == test_data[i][1], 'У исключения неправильный тип'

        print('Всё ок')


if __name__ == '__main__':
    unittest.main()
