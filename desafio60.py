n = int(input('digite o valor: '))
y = n
fat = n
if n == 0 or n == 1:
    n = 1
else:
    while n > 1:
        fat *= (n-1)
        n -= 1
print('fatorial de {} eh {}'.format(y, fat))

