# number = 1
# string = 'Hello'
#
# def global_changes():
#     global number
#     global string
#     number = 5
#     string = 'Hello, dear friend'
#     return number, string
# global_changes()
# print(number)
# print(string)
# print(global_changes())

# def global_function():
#   msg = 1
#   def local_function():
#     nonlocal msg
#     msg = 2
#     print(msg, 'local1')
#     return msg
#   print(msg, 'local2')
#   local_function()
#   print(msg, 'gloval1')
#   return msg
# global_function()
# print(global_function(), 'конечный результат')

# import math
# class Segment:
#         def __init__(self, x, y):
#             self.x = x
#             self.y = y
#         def length(self):
#             sum = math.sqrt((self.y[0]-self.x[0])**2+(self.y[1]-self.x[1])**2)   ## y[0] = x2, x[0] = x1, y[1] = y2, x[1] = y1
#             round_sum = round(sum, 2)
#             return round_sum
#         def x_axis_intersection(self):
#             if self.y[0] < 0 and self.x[0] < 0:
#                 return False
#             elif self.y[0] > 0 and self.x[0] > 0:
#                 return False
#             else:
#                 return True
#         def y_axis_intersection(self):
#             if self.y[1] < 0 and self.x[1] < 0:
#                 return False
#             elif self.y[1] > 0 and self.x[1] > 0:
#                 return False
#             else:
#                 return True
# koor = Segment((-1, 2), (3, -4))
# s = (koor.x, koor.y)
# leng = Segment.length(koor)
# print(koor.x[0])
# print(s)
# print(leng)
# x_axis = Segment.x_axis_intersection(koor)
# print(x_axis)
# y_axis = Segment.y_axis_intersection(koor)
# print(y_axis)

# class PersonInfo:
#     def __init__(self, name, num, *subdivision):
#         self.name = name
#         self.num = num
#         self.subdivision = subdivision
#
#     def short_name(self):
#         return (f'{self.name.split()[1]}' + ' ' + self.name[0] + '.')
#
#     def path_deps(self):
#         words = ''
#         counter = 0
#         for i in self.subdivision:
#             words = words + f'{self.subdivision[counter]} ' + '--> '
#             counter = counter + 1
#         return words[:-5]
#
#     def new_salary(self):
#         s = self.subdivision
#         list_dict = {}
#         for i in s:
#             print(i)
#             for sym in i:
#                 if sym in list_dict:
#                     list_dict[sym] = list_dict.get(sym) + 1
#                 else:
#                     print(sym)
#                     list_dict[sym] = 1
#         print(list_dict)
#         s = list_dict.values()
#         sorted_num = sorted(list_dict.values())
#         sorted_tree = sorted_num[:-4:-1]
#         print(sorted_tree)
#         summ = sorted_tree[0] + sorted_tree[1] + sorted_tree[2]
#         return 1337 * self.num * summ

# Persona1 = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
# print(Persona1.short_name())
# print(Persona1.path_deps())
# print(Persona1.new_salary())

# class PublicTransport:
#     def __init__(self, brand, engine_power, year, color, max_speed):
#         self.brand = brand
#         self._engine_power = engine_power
#         self.year = year
#         self.color = color
#         self.max_speed = max_speed
#     @property
#     def info(self):
#         # s = f'{self.brand} ' + f'{self.color} ' + f'{self.year} ' + f'{self._engine_power}'
#         # s = self.brand, self.color, self.year, self._engine_power
#         # return s
#         print(f'{self.brand}\n{self.color}\n{self.year}\n{self._engine_power}')
# class Bus(PublicTransport):
#     def __init__(self, brand, engine_power, year, color, max_speed, passengers, park, fare):
#         super().__init__(brand, engine_power, year, color, max_speed)
#         self.passengers = passengers
#         self.__park = park
#         self._fare = fare
#
#     @property
#     def park(self):
#         return self.__park
#     @park.setter
#     def park(self, park):
#         assert park <= 9999 and park >= 1000
#         self.__park = park
#
#
# class Tram(PublicTransport):
#     def __init__(self, brand, engine_power, year, color, max_speed, route, path, fare):
#         super().__init__(brand, engine_power, year, color, max_speed)
#         self.__route = route
#         self.path = path
#         self._fare = fare
#
#     @property
#     def how_long(self):
#         return self.max_speed/(4*self.path)
#
# car = PublicTransport('audi', 333, 2012, 'red', 350)
# bus = Bus('audi', 250, 2000, 'blue', 100, 20, 1000, 30)
# bus.park = 999
#
# trum = Tram('audi', 333, 2012, 'red', 350, 1233, 50, 50)
#
# # print(car.brand)
# # car.info
# # print(bus.max_speed)
# # print(car.max_speed)
# print(bus.park)
# print(trum.how_long)

# our_tuple = (1, 3, 2)
# def treatment_sum(our_tuple):
#     try:
#         if len(our_tuple) <= 1:
#             print(our_tuple[3])
#         elif len(our_tuple) >= 3:
#             raise Exception('Много данных')
#         else:
#             result = our_tuple[0] + our_tuple[1]
#             return result
#     except TypeError:
#         return 'Нельзя сложить эти данные'
#     except IndexError:
#         return 'Недостаточно данных'
#
# s = treatment_sum(our_tuple)
# print(s)

# class Trigon:
#     def __init__(self, *args):
#         self.args = args
#
#     def date_type(self):
#         try:
#             for i in self.args:
#                 if type(i) != int:
#                     7 + 'd'  # если данные не int создаем исключение
#         except TypeError:
#             return 'Стороны должны быть числами'
#         else:
#             return 'Все данные int'
#
#     def date_value(self):
#         try:
#             for i in self.args:
#                 if i <= 0:
#                     (int('Data'))
#         except ValueError:
#             return 'Стороны должны быть положительными'
#         else:
#             return 'Все cтороны положительные'
#
#     def trigon_true(self):
#         try:
#             if self.args[0] >= self.args[1] + self.args[2]:
#                 6/0
#             elif self.args[1] >= self.args[2] + self.args[0]:
#                 6/0
#             elif self.args[2] >= self.args[1] + self.args[0]:
#                 6/0
#         except Exception:
#             return "Не треугольник"
#         else:
#             return 'Треугольник можно построить с переданными значениями'
#
#     def trigon_arg(self):
#         n = 0
#         for i in self.args:
#             n = n + 1
#         try:
#             if n != 3:
#                 print(self.args[-55551])
#         except IndexError:
#             return f'Передано {n} аргументов, а ожидается 3'
#         else:
#             return "Всё хорошо, передано правильное количество сторон для треугольника"
#
# trey = Trigon( 1, 1, 1)
#
# print(trey.date_type())
# print(trey.date_value())
# print(trey.trigon_true())
# print(trey.trigon_arg())

# def segment(*args):
#     list_app = []
#     try:
#         for i in args:
#             for n in i:
#                 if type(n) == int:
#                     list_app.append(n)
#                 elif type(n) == str:
#                     n = int(n)
#                     7 + 'c'
#                 else:
#                     7 + 'c'
#     except TypeError:
#         s = "unsupported operand type(s) for +: 'int' and 'str'"
#         return s[::-1]
#     except ValueError:
#         s = 'can only concatenate str (not "int") to str'
#         return s[::-1]
#     else:
#         sum = 0
#         for i in list_app:
#             sum = sum + i
#         return sum
#
# print(segment(('1', 3), (4, 5)))
