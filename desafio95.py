jogador = dict()
listaJogadores = list()

while True:
    jogador['nome'] = str(input('digite o nome do jogador: '))
    jogador['qtdPartidas'] = int(input('digite a quantidade de partidas: '))

    listaGols = list()

    for c in range(0, jogador['qtdPartidas']):
        listaGols.append(int(input(f'digite a quantida de gols na {c + 1}° partida: ')))

    soma = 0

    for v in listaGols:
        soma += v

    jogador['listaGols'] = listaGols
    jogador['totalGols'] = soma

    listaJogadores.append(jogador.copy())

    opcao = str(input('deseja continuar?[S/N]: '))

    if opcao.upper() != 'S':
        break

    print('-=' * 43)

print('cod nome', ' ' * 15, 'gols', ' ' * 10, 'total')
print('-' * 49)

for c, p in enumerate(listaJogadores):
    print(f'{c}\t{p["nome"] : <20}', end='')
    print(f'{p["listaGols"]}', end=f'{" ": <16}')
    print(f'{p["totalGols"] }')

print('-' * 49)
print(listaJogadores)

while True:

    opcao = int(input('mostrar qual jogador ?[999 sai do programa]: '))

    if opcao == 999:
        break
    elif opcao > len(listaJogadores) - 1 or opcao < 0:
        print('valor inválido')
    else:
        print(f'o jogador {listaJogadores[opcao]["nome"]}  jogou em {listaJogadores[opcao]["qtdPartidas"]} '
              f'partidas e fez '
              f'{listaJogadores[opcao]["totalGols"]} gols')

        for c, g in enumerate(listaJogadores[opcao]['listaGols']):
            print(f'\tna {c + 1}° partida o jogador fez {g} gols')
