s = 0
while True:
    n = int(input('digite um número: '))
    if n == 999:
        break
    s += n
print(f'o somatório é \033[33m{s}')
