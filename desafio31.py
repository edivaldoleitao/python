dist = float(input('digite a quantidade de km da viagi'))
if dist > 200:
    preco = dist*0.45
else:
    preco = dist*0.5
print('o valor foi de {} R$'.format(preco))
