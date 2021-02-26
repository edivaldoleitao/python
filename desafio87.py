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

print('-=' * 20)
soma = 0
for c in range(0, 3):
    for v in range(0, 3):
        if lista[c][v][0] % 2 == 0:
            soma += lista[c][v][0]
print(f'o valor da soma dos pares é {soma}')
somaColuna = 0
for c in lista:
    somaColuna += c[2][0]

print(f'a soma das coluna 3 é {somaColuna}')
maior = 0
for c in range(0, 3):
    if c == 0:
        maior = lista[1][c][0]
    elif maior < lista[1][c][0]:
        maior = lista[1][c][0]

print(f'o maior número da 2° linha é {maior}')
