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
# # print("Weight", type(sys.argv))#тип лист
# # print("a list", sys.argv)#вывод самого списка
# # print('80' in sys.argv)#наличие '80' в списке
# # print('80' not in sys.argv)
# # len(), min(), max() and etc..
# # print(sys.argv.index('80'))

# a_string = 'Z cnhjrf, fdcjdc, dccjd/'
# list = ['aa', 'bb', 'cc', 672364, [1, 2, 3, 'ty']]
# # print(dir(list))
# print(len(list))
# print(a_string)
# a_list = a_string.split('c')

# a_list.append('12345')
# print(a_list)

# a_list[1] = 'список!'
# a_list.remove('12345')
# print(a_list)

# del a_list
# print(a_list)
# #4) Кортежи(tuple)
# t = (1,)
# print(type(t))
# a, b, c = ('s','d',1)

# print(a,"\n",b,"\n", c)

# # 5) Словари - похожие на списки. Хранят ключ:значение. Ключ - неименияемый тип данных(int, float, string, tuple).
# d =dict(
#     света=27, 
#     Юра=30, 
#     Саша=18)
# print(d)
# print(str(d['света']) + ' y.o.')


# 6) Множество(set)
s = set()
print(type(s))
s.add(1)
s.add('www')
print(s)


#7)Операторы сравнения. Булевый тип.
# False 
# a = True
# print(type(a))
# print(True == True)
# b = 5
# c = 5
# print(a == c)

# a = 'dd'
# b = 'asdasddd'
# # print(a not in b)

# print(2 > 3 and 100 == 100)
# print(5 < 3 or 100 == 100)
# #AND(*-умножение) ИМЕЕТ ВЫЩЕ ПРИОРИТЕТ, ЧЕМ OR(+ - сложение)! NOT - обращает значение переменной на противоположное.
# toggler = False
# #cicle
# toggler = not toggler 

# z = 0
# a = z or 'Anon' or 'vasia'
# print(a)

# result = i or "WER"
# # print(result)
# i = int(input('Введите число: '))
# if i < 100 :
#     print('+++++++++++++')
# else:
#     print('--------------')

# #CASE аналог в Python
# a = {1: 'ssss', 2:'ss'}
# a.get(1, 'nfrjuj pyfxtybz ytn')
# a.get(3, 'sdsfsdgsdfdfg')
# print(a)

# i = 0 #
# while i <= 10:
#     print(i)
#     i +=1


