x = float(input('digite o 1° valor: '))
y = float(input('digite o 2° valor: '))
opcao = 0
while opcao != 5:
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
    opcao = int(input(''))
    if opcao == 1:
        print('a soma entre {:.1f} e {:.1f} eh {:.1f}\n'.format(x, y, x+y))
    elif opcao == 2:
        print('a multiplicação dos valores {} e {} eh {}\n'.format(x, y, x*y))
    elif opcao == 3:
        if x > y:
            print('{} eh o maior!\n'.format(x))
        else:
            print('{} eh o maior!\n'.format(y))
    elif opcao == 4:
        x = float(input('insira um novo valor: \n'))
        y = float(input('insira um segundo novo valor: \n'))
print('FIM DO PROGRAMA!')
