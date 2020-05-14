# def my_func():
#     print("My name is Sergey")
# my_func()

# def my_func(name):
#     print("My name is {}".format(name))
# my_func("Sergey")

# def my_func(firstname, lastname, age, weight):
#     print("My name is {}".format(firstname))
#     print("My lastname is {}".format(lastname))
#     print("My age is {}".format(age))
#     print("My weight is {}".format(weight))
# my_func('Sergei', 'Vertinskiy',23, 85)
# my_func(firstname='Sergey', lastname='Vertinskiy', age=43, weight=95)


# help(print)

# def mul(a):
#     #Переменная a залипла здесь!
#     def helper(b):
#         return a * b
#     return helper
# mul_5 = mul(5)
# print(mul_5(3))

####ФАЙЛЫ


fp = open('textfile.txt', 'r')
print(type(fp))
# print(fp.read())
print(fp.readline())





  

# fp.write(ipaddr)
    # for ip in ipaddr:
    #     fp.write(data)

    # data_ip = {}.fromkeys(data, 0)
    # for a in data:
    #     data_ip[a] += 1
    # print(data_ip)
    # count = Counter(ipaddr)
    # print (count)



# while line:
#     print(line)
#     line = f.readline()
# f.close
