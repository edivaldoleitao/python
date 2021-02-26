import random

jogos = list()
nJogos = int(input('digite quantos jogos deseja fazer: '))
jogo = list()

for c in range(0, nJogos):
    for j in range(0, 6):
        jogo.append(random.randint(0, 60))
    jogos.append(jogo[:])
    jogo.clear()

print('os jogos sorteados foram: ')

for v, c in enumerate(jogos):
    print(f'jogo {v + 1}: {c}')
