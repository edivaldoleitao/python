frase = str(input('digite qualquer frase ou plavra:'))
frase2 =''
for c in range(len(frase) - 1, -1, -1):
    if frase[c] != " ":
        frase2 += frase[c]
if frase.replace(' ', '') == frase2:
    print('palindromo')
else:
    print('nao palindromo')
print('{} e {}'.format(frase, frase2))
