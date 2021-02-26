n = int(input('digite até que posição na sequencia de fibbonacci vc quer ver: '))
cont = 0
fib1 = 0
fib2 = 1
fib3 = 0
while cont < n:
    if cont == 0:
        fib3 = fib1
    elif cont == 1:
        fib3 = fib2
    else:
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
    print(fib3, end=' ')
    cont += 1

