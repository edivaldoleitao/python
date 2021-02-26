import random
print('jokenpô')
opcaoNum = int(input('escolha uma opção: \n1-pedra \n2-papel \n3-tesoura'))
escolhas = ['pedra', 'papel', 'tesoura']
escolhaMaquina = random.choice(escolhas)
opcao = escolhas[opcaoNum - 1]
print('voçê escolheu {} e o computador escolheu {}'.format(opcao, escolhaMaquina))
if opcao == escolhaMaquina:
    print('empate!')
elif opcao == 'pedra' and escolhaMaquina == 'tesoura':
    print('\033[1;32mvoçê ganhou!')
elif opcao == 'papel ' and escolhaMaquina == 'pedra':
    print('\033[1;32mvoçê ganhou!!')
elif opcao == 'tesoura' and escolhaMaquina == 'papel':
    print('\033[1;32mvoçê ganhou!')
else:
    print('\033[1;31mvoçê perdeu!!!')
