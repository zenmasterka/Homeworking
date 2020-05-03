m = float(input("Введите ваш вес(кг.): "))
h = float(input("Введите ваш рост(м.): "))
i = (m) / (h * h)
print('Индекс массы тела:',i)
scale = '20' + "="*int(i-20) + "|" + "="*int(50-i) + "50"
print(scale)

