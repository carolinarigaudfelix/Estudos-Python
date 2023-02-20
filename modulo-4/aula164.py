# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

fmt ='%d/%m/%Y'
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime('%d/%m/%Y'))
print(data.strftime('%Y-%m-%d'))
print(data.strftime('%Y-%m-%d %H:%M:%S'))
print(type(data.strftime('%Y-%m-%d %H:%M:%S')))
print(data.strftime('%Y'), data.month)



