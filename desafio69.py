contIdade = 0
contH = 0
contM = 0
while True:
    idade = int(input('digite a idade da pessoa: '))
    sexo = str(input('digite o sexo da pessoa[M/F]: '))
    if idade >= 18:
        contIdade += 1
    if sexo.upper() == 'M':
        contH +=1
    if sexo.upper() == 'F' and idade >= 20:
        contM += 1
    opcao = str(input('deseja continuar?[S/N]: '))
    if opcao.upper() != 'S':
        break
print(f'a quantidade de pessoas com mais de 18 anos é {contIdade}')
print(f'a quantidade de homens é {contH}')
print(f'a quantidade de mulheres com mais de 20 anos é {contM}')

