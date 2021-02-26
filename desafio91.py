import random
from operator import itemgetter

valoresDado = {'jogador1': random.randint(1, 6), 'jogador2': random.randint(1, 6), 'jogador3': random.randint(1, 6),
               'jogador4': random.randint(1, 6)}

for k, v in valoresDado.items():
    print(f'o {k} tirou {v}')

# para sortear pelo valor do dicionário precisa usar o itemgetter na key, na verdade o tornando numa lista XP
# a posicao da chave é 0 e do valor é 1 para o item

sorted_valoresdado = sorted(valoresDado.items(), key=itemgetter(1), reverse=True)

print('-=' * 23)
print(f'{"SORTEADO" : ^46}')

for i, v in enumerate(sorted_valoresdado):
    print(f'{i + 1}° lugar {v[0]} com {v[1]}')
