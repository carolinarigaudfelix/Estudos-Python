# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

# 60 parcelas

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos


data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas

for data  in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:.2f}')

# print(numero_parcelas)
# print(f'{valor_parcela:.2f}')

print(f'Você pegou R${valor_total:,.2f} para pagar em {5} anos\n\
      ({numero_parcelas}meses) em parcelas de R${valor_parcela:.2f}')