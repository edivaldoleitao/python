lista = []
while True:
    lista.append(int(input('digite um valor: ')))
    continuar = str(input('deseja continuar?[S/N]: '))
    if continuar.upper() != 'S':
        break
print(f'\na lista contém 5 ? {lista.__contains__(5)}')
print(f'foram digitados {len(lista)} números')
lista.sort(reverse=True)
print('a lista na ordem inversa: ', lista)
