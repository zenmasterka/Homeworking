import itertools
def my_gen():
    for i in itertools.count(0):
        if i == 0:
            yield i
        elif i % 3 == 0:
            yield 'Василий'
        else:
            yield i
g1 = my_gen()
# a = next(g1)
# b = next(g1)
# c = next(g1)
# d = next(g1)
# e = next(g1)
# f = next(g1)
# g = next(g1)
# h = next(g1)
# i = next(g1)
# j = next(g1)
# k = next(g1)
# print(a,b,c,d,e,f,g,h,i,j,k)
for x in g1:
    print("TRY", x)
    if x > '15':
        break
# for x in g1:
#     print("TRY", x)
#     break
# for x in g1:
#     print("TRY", x)
#     break
# for x in g1:
#     print("TRY", x)
#     break
# for x in g1:
#     print("TRY", x)
#     break
# for x in g1:
#     print("TRY", x)
#     break
# for x in g1:
#     print("TRY", x)
#     break
# for x in g1:
#     print("TRY", x)
#     break

# while i < 1000:
    #     if i % 3 == 0:
    #         yield 'Vasia'
#     i = 0
#     while i < n:
#         if (i % 3) == 0:
#              print("Вася")
#         else:
#             print(i)
#     yield i
#     i += 1
#     print(i)
# my_gen()




# import itertools
# my_gen = (x for x in itertools.count())
# x=0
# for x in my_gen:
#     if x % 3 == 0:
#         print("Vasia")
#     else:
#         print(x)
#     if x==10:
#         break




