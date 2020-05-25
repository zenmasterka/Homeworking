import time
import datetime
symbol = '\u2593'
def zero():
    print(symbol*8)
    print(symbol*2 + '    ' + symbol*2)
    print(symbol*2 + '    ' + symbol*2)
    print(symbol*2 + '    ' + symbol*2)
    print(symbol*8)
def one():
    print(symbol*5)
    print('   ' + symbol*2 + '   ')
    print('   ' + symbol*2 + '   ')
    print('   ' + symbol*2 + '   ')
    print(symbol*8)
def two():
    print(symbol*8)
    print('      ' + symbol*2)
    print(symbol*8)
    print(symbol*2 + '      ')
    print(symbol*8)
def three():
    print(symbol*8)
    print('      ' + symbol*2)
    print(symbol*8)
    print('      ' + symbol*2)
    print(symbol*8)
def four():
    print(symbol*2 + '    ' + symbol*2)
    print(symbol*2 + '    ' + symbol*2)
    print(symbol*8)
    print('      ' + symbol*2)
    print('      ' + symbol*2)
def five():
    print(symbol*8)
    print(symbol*2 + '      ')
    print(symbol*8)
    print('      ' + symbol*2)
    print(symbol*8)
def six():
    print(symbol*8)
    print(symbol*2 + '      ')
    print(symbol*8)
    print(symbol*2 + '    ' + symbol*2)
    print(symbol*8)
def seven():
    print(symbol*8)
    print(symbol*2 + '      ')
    print(symbol*2 + '      ')
    print(symbol*2 + '      ')
    print(symbol*2 + '      ')
def eight():
    print(symbol*8)
    print(symbol*2 + '    ' + symbol*2)
    print(symbol*8)
    print(symbol*2 + '    ' + symbol*2)
    print(symbol*8)
def nine():
    print(symbol*8)
    print(symbol*2 + '    ' + symbol*2)
    print(symbol*8)
    print('      ' + symbol*2)
    print(symbol*8)
def point():
    print('        ')
    print('   ' + symbol*2 + '   ')
    print('        ')
    print('   ' + symbol*2 + '   ')
    print('        ')
# a = one()
# b = two()
# c = three()
# d = four()
# e = five()
# f = six()
# g = seven()
# h = eight()
# i = nine()
while True:
    now = datetime.datetime.now().time()
    str_now = list(now.strftime('%H.%M.%S'))
    asd = []
    for e in str_now:
        if e == '1':
            e = one()
            asd.append(e)
        elif e == '2':
            e = two()
            asd.append(e)
        elif e == '3':
            e = three()
            asd.append(e)
        elif e == '4':
            e = four()
            asd.append(e)
        elif e == '5':
            e = five()
            asd.append(e)
        elif e == '6':
            e = six()
            asd.append(e)
        elif e == '7':
            e = seven()
            asd.append(e)
        elif e == '8':
            e = eight()
            asd.append(e)
        elif e == '9':
            e = nine()
            asd.append(e)
        elif e == '0':
            e = zero()
            asd.append(e)
        elif e == '.':
            e = point()
            asd.append(e)
    time.sleep(1)
# print(str_now)
# print(asd[1])

    


# print(a, b, c, d, e, f, g, h, i)
# while True:
#     if str_now[0] == '1':
#         print(a)
#     if str_now[0] == '2':
#         print[b]
#     else:
#         break
