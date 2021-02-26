n = 0
x = 0
while x != 999:
    x = int(input('digite um numero pra ser somado/\033[34m[999 -> flag de saída]\033[m: '))
    if x != 999:
        n += x
    print('somatorio: \033[33m{}\033[m'.format(n))
print('fim')
