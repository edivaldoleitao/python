list = []
while True:
    elemento = int(input('adicione um valor a lista: '))
    if not list.__contains__(elemento):
        list.append(elemento)
    continuar = str(input('deseja continuar ?[S/N]: '))
    if continuar.upper() != 'S':
        break
list.sort()
print(f'lista em ordem: {list}')

