a = 'D:\Programming\python\\autotests_course_example\9\\test_file\\task1_data.txt'
f = open(a, mode='r', encoding='utf-8')
text_read = f.read()
list_res = ''
for i in text_read:
    if i not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        list_res = list_res + i

b = 'D:\Programming\python\\autotests_course_example\9\\test_file\\task1_answer.txt'
f = open(b, mode='w', encoding='utf-8')
f.write(list_res)
f.close()
