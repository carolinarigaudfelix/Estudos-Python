"""
Imprecisão de ponto flutuante
Double-precision floating-point
"""

import decimal

numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.5)
numero_3 = numero_1 + numero_2


print(f'{numero_3:.2f}')
print(round(numero_3, 2))