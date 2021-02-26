speed = float(input('digite sua velocidade:'))

if speed > 80:
    print('sua multa eh de {:.2f} R$ , seu trouxa!'.format((speed - 80)*7))
else:
    print('pof!')
