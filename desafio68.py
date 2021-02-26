import random
vitorias = 0
while True:
    numPC = random.randrange(0, 6)
    escolha = str(input('escolha ímpar ou par[I/P]: '))
    numero = int(input('digite um numero entre 0 e 5: '))
    soma = numero + numPC
    if (soma % 2 == 1) and escolha.upper() == 'I':
        print(f'voçê escolheu {numero} e a máquina escolheu {numPC}')
        print('\033[32mYOU WIN !!\033[m')

    elif (soma % 2 == 0) and escolha.upper() == 'P':
        print(f'voçê escolheu {numero} e a máquina escolheu {numPC}')
        print('\033[32mYOU WIN!!\033[m')
    else:
        print(f'voçê escolheu {numero} e a máquina escolheu {numPC}')
        print('\033[31mYOU LOSE!!!\033[m')
        break

    vitorias +=1
print(f'\033[1;32mvitórias seguidas: {vitorias}')



