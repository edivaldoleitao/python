ano = int(input('digite o ano:'))
if (ano % 4 == 0 and ano % 100 != 100) or ( ano % 400 == 0):
    print('ano bissexo')
else:
    print('ano não bissexo')
