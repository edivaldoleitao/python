a = int(input('digite o valor do lado A:'))
b = int(input('digite o valor do lado B:'))
c = int(input('digite o valor do lado C:'))
if a + b > c and a + c > b and c + b > a:
    if a == b == c:
        print('triângulo equilátero')
    elif a == b or a == c or c == b:
        print('triângulo isósceles')
    else:
        print('triângulo escaleno')
else:
    print('não é um triângulo!')

