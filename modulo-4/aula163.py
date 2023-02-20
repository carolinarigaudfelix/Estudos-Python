# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('17/08/2003 09:30:30', fmt)
data_fim = datetime.strptime('02/03/1996 08:20:20', fmt)
delta = timedelta(days=10, hours =2)
delta = relativedelta(data_inicio, data_fim)
print(delta.days, delta.years)
# print(data_fim - delta)
#print(data_fim + relativedelta(seconds=60, minutes=10))
# delta = data_fim - data_inicio
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds()) #é um objeto de diferença entre 2 datas

delta = timedelta(days=10, hours=2)
print(data_fim + delta) #comparações

#INSTALAR DATEUTIL - pip install python-dateutil types-python-dateutil