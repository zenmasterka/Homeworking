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


#Проверка:
a = next(g1)
b = next(g1)
c = next(g1)
d = next(g1)
e = next(g1)
f = next(g1)
g = next(g1)
h = next(g1)
i = next(g1)
j = next(g1)
k = next(g1)
print(a,b,c,d,e,f,g,h,i,j,k)