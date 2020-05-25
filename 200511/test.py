# import Parser
import datetime

# print(dir(datetime))
r = datetime.date(1996, 12, 4)
today = datetime.date.today()
print(today - r)

tn = datetime.datetime.now()
print(tn) 
str_tn = tn.strftime('%d.%Y.%A %H.%M.%S')
print(str_tn)
time_as_str = '18.05.19 13:27'
time_obj = datetime.datetime.strptime('1805191327', '%d%m%y%H%M')
print(time_obj)
