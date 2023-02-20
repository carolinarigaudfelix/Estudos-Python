# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz #lista de timezones

from datetime import datetime

from pytz import timezone


# data_str = '2022-04-20 07:49:23'
# data_str_fmt = '%Y-%m-%d %H:%M:%S' #a data deve ter o formato exigido

# data_str_data = '02/04/2023'
# data_str_fmt = '%d/%m/%Y'


data =datetime.now(timezone('Asia/Tokyo')) 
print(data.timestamp()) #fala os numeros de segundos de 1970 até hj da pra fazer
#uma data com isso
print(datetime.fromtimestamp(1676907222))

#é importante trabalhar o timezone vc passa
#  isso como parâmetro da função

# data = datetime.strptime(data_str_data, data_str_fmt)
#data = datetime(2022, 4, 20 ,7,49,23)
