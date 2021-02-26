lista = [[], [], []]

for c in range(0, 3):
    for v in range(0, 3):
        dado = list()
        dado.append(int(input(f'digite o valor na célula [{c}, {v}]: ')))
        lista[c].append(dado[:])
        dado.clear()
print('-=' * 20)
for c in range(0, 3):
    for v in lista[c]:
        print(v, end=' ')
    print('')
