valor1 = int(input('digite um valor: '))
valor2 = int(input('digite um valor: '))
valor3 = int(input('digite um valor: '))
valor4 = int(input('digite um valor: '))

numeros = (valor1, valor2, valor3, valor4)

print(f'o número 9 apareceu {numeros.count(9)} vezes')
print(f'posição do primeiro 3 é {numeros.index(3)}')
print('os números pares:', end=' ')
for valor in numeros:
    if valor % 2 == 0:
        print(valor, end=' ')
