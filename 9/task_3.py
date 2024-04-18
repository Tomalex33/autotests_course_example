
# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

a = 'C:\\Users\\ap.tomchik\PycharmProjects\Автотестирование2023\9\\test_file\\task_33.txt'
f = open(a, mode='a+', encoding='utf-8')

f.seek(0)
text_read = f.readlines()

print(text_read)


list_sum = []
spisok = []
for i in text_read:
    if i == '\n':

        print(spisok, "список для среза")
        sum = 0
        for b in spisok:
            sum = sum + b

        print(sum, "сумма одной покупки")

        list_sum.append(sum)
        print(list_sum, "список сумм")
        spisok = []
        print(spisok, "spisok после среза")
    else:

        i[:-1]
        num = int(i)
        spisok.append(num)
        print(spisok)

print(list_sum)

# list_number = []
# for i in text_read:
#     if i != '\n':
#         i[:-1]
#         num = int(i)
#         list_number.append(num)
# s = sorted(list_number)
# print(s)
# print(s[::-1])
# sum1 = s[-3]
# sum2 = s[-2]
# sum3 = s[-1]
# sum = []
# sum.append(s[-3])
# sum.append(s[-2])
# sum.append(s[-1])
# print(sum)
# three_most_expensive_purchases = sum[0] + sum[1] + sum[2]
# print(three_most_expensive_purchases)

assert three_most_expensive_purchases == 202346

