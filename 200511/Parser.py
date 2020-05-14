import json
from collections import Counter
log = 'd:/Python/Repositirie/Homeworking/200511/LOGS_APACHE.txt'
pars = 'd:/Python/Repositirie/Homeworking/200511/data.txt'
data = []
f = open(log, 'r+')
f.seek(0)
lines = f.readlines()
for line in lines:
    conn_data=line.split(' ')
    ipaddr=conn_data[0].strip()
    data.append((ipaddr))
#Количество строк
for line in lines:
    kol_str=len(lines)
print("Количество строк:", kol_str)
#количество уникальных IP
ip = set(data)
print("Количество уникальных IP:", len(ip))
fp = open(pars, 'r+')
#вывод уникальных IP в программе
#print("Уникальные IP адреса:", ip)
#Вывод уникальных ip в файл
fp.write("Уникальные IP")
fp.write("\n")
for i in ip:
    fp.write(str(i))
    fp.write("\n")
#вывод количество запросов с различных браузеров
f.seek(0)
s, c, m = 0, 0, 0
for line in lines:
    if "Safari" in line:
        s+=1
    if "Mozilla" in line:
        m+=1
    if "Chrome" in line:
        c+=1
print("Количество обращений с браузера Safari:", s)
print("Количество обращений с браузера Chrome:", c)
print("Количество обращений с браузера Mozilla:", m)
fp.seek(0)
f.close()
fp.close()

  