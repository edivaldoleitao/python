maior = 0.0
menor = 0.0
for c in range(0, 5):
    x = float(input('digite um peso em \033[31mKg\33[m:'))
    if c == 0:
        menor = x
        maior = x
    else:
        if menor >= x:
            menor = x
        elif maior <= x:
            maior = x
print('maior peso {:.1f}Kg, menor peso{:.1f} Kg'.format(maior, menor))

