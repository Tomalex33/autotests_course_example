
def my_range(start, end=None):
    if end is None:
        start, end = 0, start
        yield start
        start = start + 1
        if start == end:
            raise StopIteration("end")


r = my_range(1, 5)
for i in r:
    print(type(i))
    print(i)
print(r)
