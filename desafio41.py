import datetime
anoNascimento = int(input('digite seu ano de nascimento:'))
idade = datetime.date.today().year - anoNascimento
if idade <= 9:
    print('mirim')
elif 9 < idade <= 14:
    print('infantil')
elif 14 < idade <= 19:
    print('junior')
elif 19 < idade <= 20:
    print('sênior')
else:
    print('master')
