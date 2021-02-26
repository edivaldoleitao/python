import random
numeros = ()
for c in range(0, 5):
    r = (random.randint(0, 10),)
    numeros += r
print(numeros)
print(f'o menor é: {sorted(numeros)[0]}')
print(f'o maior é: {sorted(numeros)[len(numeros) - 1]}')

