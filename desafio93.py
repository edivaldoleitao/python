jogador = dict()

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

print(jogador)
print(f'o jogador {jogador["nome"]}  jogou em {jogador["qtdPartidas"]} partidas e fez {jogador["totalGols"]} gols')

for c, g in enumerate(jogador['listaGols']):
    print(f'\tna {c + 1}° partida o jogador fez {g} gols')
