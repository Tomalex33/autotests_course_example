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

import math
class Segment:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def length(self):
            sum = math.sqrt((self.y[0]-self.x[0])**2+(self.y[1]-self.x[1])**2)   ## y[0] = x2, x[0] = x1, y[1] = y2, x[1] = y1
            round_sum = round(sum, 2)
            return round_sum
        def x_axis_intersection(self):
            if self.y[0] < 0 and self.x[0] < 0:
                return False
            elif self.y[0] > 0 and self.x[0] > 0:
                return False
            else:
                return True
        def y_axis_intersection(self):
            if self.y[1] < 0 and self.x[1] < 0:
                return False
            elif self.y[1] > 0 and self.x[1] > 0:
                return False
            else:
                return True
koor = Segment((-1, 2), (3, -4))
s = (koor.x, koor.y)
leng = Segment.length(koor)
print(koor.x[0])
print(s)
print(leng)
x_axis = Segment.x_axis_intersection(koor)
print(x_axis)
y_axis = Segment.y_axis_intersection(koor)
print(y_axis)
