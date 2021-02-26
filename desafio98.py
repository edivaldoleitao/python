def contador(inicio, fim, passo):

    if inicio <= fim + 1:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ')
            cont += passo
    elif inicio >= fim + 1:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ')
            cont -= passo


# PROGRAMA MAIN

contador(1, 10, 1)
print()
contador(0, 10, 2)
print()
inicio = int(input('digite o início: '))
fim = int(input('digite o fim: '))
passo = int(input('digite o passo: '))
contador(inicio, fim, passo)
