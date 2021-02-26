peso = float(input('digite seu peso:'))
altura = float(input('digite sua altura'))
imc = peso/(altura**2)
if imc < 18.5:
    print('abaixo do peso')
elif 18.5 <= imc < 25:
    print('peso ideal')
elif 25 <= imc < 30:
    print('sobrepeso')
elif 30 <= imc <= 40:
    print('obesidade')
else:
    print('obesidade mórbida')
print('seu imc : {:.2f}'.format(imc))

