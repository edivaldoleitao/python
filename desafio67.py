while True:
    n = int(input('digite um valor pra tabela: '))
    if n < 0:
        break
    cont = 1
    while cont < 11:
        print(f'{n} x {cont} = {cont*n}')
        cont += 1
print('\033[31mFIM!!')
