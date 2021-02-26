lista = [[], []]
for c in range(0, 7):
    numero = int(input('digite um valor: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
lista[0].sort()
lista[1].sort()
print('valores pares: ', end='')
for v in lista[0]:
    print(v, end=' ')
print('')
print('valores ímpares: ', end=' ')
for l in lista[1]:
    print(l, end=' ')



