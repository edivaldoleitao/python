import random
rand = random.randrange(1, 11)
escolha = 0
countTentativas = 1
while escolha != rand:
    escolha = int(input('digite um inteiro entre 1 e 10: '))
    if escolha != rand:
        countTentativas += 1
print('voçê tentou {} veze(s) o número era {}'.format(countTentativas, rand))
