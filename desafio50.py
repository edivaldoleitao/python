x = 0
for c in range(0, 6):
    n = int(input('digite um numero:'))
    if n % 2 == 0:
        x += n
print('o somatório eh {}:'.format(x))
