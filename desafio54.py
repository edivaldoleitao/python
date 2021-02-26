import datetime
count = 0
for c in range(0, 7):
    anoNascimento = int(input('digite o ano de nascimentop'))
    if datetime.date.today().year - anoNascimento >= 18:
        count += 1
print('existem {} pessoas que são adultos, e {} que não são'.format(count, 7 - count))
