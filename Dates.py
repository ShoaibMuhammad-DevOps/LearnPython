import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.hour)
print(x.day)
print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%C"))
print(x.strftime("%D"))


x = datetime.datetime(2022, 4, 22)
print(x)