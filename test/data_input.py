import os
import sys

#
pass
#
# 1) запрос данных у пользователя


# user_weght = input(".Введите ваш вес: ")
# user_height = input(".Введите ваш рост: ")



# print("Сумма введенных данных: ", float(user_weght) + float(user_height))


# 2)загрузка данных а процессе запуска скрипта
# print("Weight", type(sys.argv[1]))
# print("Height", sys.argv[2])
# d:/Python/Repositirie/Homeworking/test/data_input.py 80 200
# Weight <class 'str'>
# Height 200

# 3) Списки(List)
# print("Weight", type(sys.argv))#тип лист
# print("a list", sys.argv)#вывод самого списка
# print('80' in sys.argv)#наличие '80' в списке
# print('80' not in sys.argv)
#len(), min(), max() and etc..
# print(sys.argv.index('80'))

a_string = 'Z cnhjrf, fdcjdc, dccjd/'
list = ['aa', 'bb', 'cc', 672364, [1, 2, 3, 'ty']]
# print(dir(list))
print(len(list))
print(a_string)
a_list = a_string.split('c')

a_list.append('12345')
print(a_list)

a_list[1] = 'список!'
a_list.remove('12345')
print(a_list)

# del a_list
# print(a_list)

