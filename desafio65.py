maior = 0
menor = 0
opcao = 's'
s = 0
cont = 0
while opcao != 'N':
    n = int(input('insira um número: \n'))

    if cont == 0:
        menor = menor = n

    if maior <= n:
        maior = n
    elif menor >= n:
        menor = n

    s += n
    cont += 1
    print('somatório: {}'.format(s))
    print('o maior é {} , e o menor é {}'.format(maior, menor))
    print('a média dos números é {:.2f}\n'.format(s / cont))
    opcao = str(input('deseja continuar?\033[32m[S/N]\033[m: \n')).upper()
print('\033[1;31;44mFIM!!!\033[m')
