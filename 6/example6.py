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
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def length(self):
        print(math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2))
koor = Segment(1, 2,3,4)
s = (koor.x1, koor.y1)
leng = Segment.length()

print(s)
print(leng)
