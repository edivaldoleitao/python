num = int(input('digte um número inteiro:'))
opcao = int(input('digite uma opção de base para coverter: \n 1-binário \n 2-octal \n 3-hexadecimal \n'))
if opcao == 1:
    print('o número {} em binário:'.format(num), bin(num))
elif opcao == 2:
    print('o número {} em octal:'.format(num), oct(num))
elif opcao == 3:
    print('o número {} em hexadecimal:'.format(num), hex(num))
else:
    print('opção inválida!')
