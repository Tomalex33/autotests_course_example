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

class PersonInfo:
    def __init__(self, name, num, *subdivision):
        self.name = name
        self.num = num
        self.subdivision = subdivision

    def short_name(self):
        return (f'{self.name.split()[1]}' + ' ' + self.name[0] + '.')

    def path_deps(self):
        words = ''
        counter = 0
        for i in self.subdivision:
            words = words + f'{self.subdivision[counter]} ' + '--> '
            counter = counter + 1
        return words[:-5]

    def new_salary(self):
        s = self.subdivision
        list_dict = {}
        for i in s:
            print(i)
            for sym in i:
                if sym in list_dict:
                    list_dict[sym] = list_dict.get(sym) + 1
                else:
                    print(sym)
                    list_dict[sym] = 1
        print(list_dict)
        s = list_dict.values()
        sorted_num = sorted(list_dict.values())
        sorted_tree = sorted_num[:-4:-1]
        print(sorted_tree)
        summ = sorted_tree[0] + sorted_tree[1] + sorted_tree[2]
        return 1337 * self.num * summ

Persona1 = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
print(Persona1.short_name())
print(Persona1.path_deps())
print(Persona1.new_salary())

# s = ('Developer', 'das', 'dsadasd', '111111')
# list_dict = {}
# for i in s:
#     print(i)
#     for sym in i:
#         if sym in list_dict:
#             list_dict[sym] = list_dict.get(sym) + 1
#         else:
#             print(sym)
#             list_dict[sym] = 1
# print(list_dict)
# s = list_dict.values()
# sorted_num = sorted(list_dict.values())
# sorted_tree = sorted_num[:-4:-1]
# print(sorted_tree)
# summ = sorted_tree[0] + sorted_tree[1] + sorted_tree[2]

