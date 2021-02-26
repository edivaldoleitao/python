import datetime
anoNascimento = int(input('digite seu ano de nascimento:'))
idade = datetime.date.today().year - anoNascimento
if idade > 18:
    print('voçê passou {} ano(s) de se alistar, mané!!'.format(idade - 18))
elif idade == 18:
    print('vai se lascar ainda esse ano!')
else:
    print('só falta {} ano(s) pra se lascar , calma!'.format(18 - idade))
