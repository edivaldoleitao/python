lista = []
while True:
    lista.append(int(input('digite um valor: ')))
    continuar = str(input('deseja continuar?[S/N]: '))
    if continuar.upper() != 'S':
        break
listaP = []
listaI = []
for item in lista:
    if item % 2 == 0:
        listaP.append(item)
    else:
        listaI.append(item)
print('lista: ', lista)
print('lista ímpar: ', listaI)
print('lista par', listaP)
