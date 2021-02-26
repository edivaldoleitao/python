a = float(input('digite a primeira nota: '))
b = float(input('digite a segunda nota: '))
media = (a + b)/2
print('sua média foi {:.1f}'.format(media))
if media >= 7:
    print('APROVADO!!')
elif 6.9 >= media >= 5:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO!!!!!!!!!!!!!!!!!!!!!!!!')

