a = 'C:\\Users\\ap.tomchik\PycharmProjects\Автотестирование2023\9\\test_file\\1.txt'
f = open(a, mode='a+', encoding='UTF-8')
# print(f.read())
text_off = f.read()
list_res = ''
for i in text_off:
    if i not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        print(list_res)
        list_res = list_res + i
print(list_res)
f.seek(0)
print(*f)
f.close()

# c = '1111ccc tyyrt 13 a 1'
# a = ''
# for i in c:
#     if i not in ('0', '1', '2', '3', '4','5','6','7','8','9'):
#         a = a + i
# print(a)
