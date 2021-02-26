idadeMedia = 0.0
countM = 0
nomeHomemVelho = ''
maior = 0.0
for c in range(0, 5):
   nome = input('digite o nome da pessoa:').strip()
   idade = int(input('digite a idade da pessoa:'))
   sexo = input('digite o sexo:').strip()
   idadeMedia += idade
   if c == 0 and sexo.lower() == 'm':
       maior = idade
       nomeHomemVelho = nome
   else:
       if maior <= idade and sexo.lower() == 'm':
           maior = idade
           nomeHomemVelho = nome
       elif idade >= 20 and sexo.lower() == 'f':
           countM += 1
idadeMedia /= 5
print('o nome do homem mais velho eh {} a quantidade de mulheres com 20 anos eh {} e a idade media eh  {}'.format(nomeHomemVelho, countM, idadeMedia))

