cedulas50 = 0
cedulas20 = 0
cedulas10 = 0
cedulas1 = 0

print('-' * 30)
print(f'{"Banco":^30}')
print('-' * 30)
saque = int(input('digite o valor a ser sacado: '))
while True:
    if saque >= 50:
        cedulas50 += 1
        saque -= 50
    elif 50 > saque >= 20:
        cedulas20 += 1
        saque -= 20
    elif 20 > saque >= 10:
        saque -= 10
        cedulas10 += 1
    elif 10 > saque >= 1:
        saque -= 1
        cedulas1 += 1
    elif saque == 0:
        break
print(f'cédulas de R$ 50: {cedulas50}')
print(f'cédulas de R$ 20: {cedulas20}')
print(f'cédulas de R$ 10: {cedulas10}')
print(f'cédulas de R$ 1: {cedulas1}')
