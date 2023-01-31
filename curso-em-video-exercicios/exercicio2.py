def mango(quantity, price):
    free= int(quantity/3)
    return (quantity-free) * price

print(mango(9,5))