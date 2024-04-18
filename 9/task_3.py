
# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

a = ('D:\Programming\python\\autotests_course_example\9\\test_file\\task_3.txt')
f = open(a, mode='a+', encoding='utf-8')
f.seek(0)
text_read = f.readlines()
list_sum = []
spisok = []
for i in text_read:
    if i == '\n':
        sum = 0
        for b in spisok:
            sum = sum + b
        list_sum.append(sum)
        spisok = []
    else:
        i[:-1]
        num = int(i)
        spisok.append(num)
s = sorted(list_sum)
three_most_expensive_purchases = s[-1] + s[-2] + s[-3]
print(three_most_expensive_purchases)

assert three_most_expensive_purchases == 202346

