a = int(input('insira o lado A:'))
b = int(input('insira o lado B:'))
c = int(input('insira o lado C:'))
if a + b > c and a + c > b and b + c > a:
    print('É um triângulo')
else:
    print('não é um triangulo')
