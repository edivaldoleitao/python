n = int(input('digite o 1° termo: '))
razao = int(input('digite o termo da progressão: '))
adicional = -1
cont = 0
nRepete = 0
while adicional != 0 and nRepete != 1:
    while cont < 10 :
        print(n)
        n += razao
        cont += 1
    adicional = int(input('desejar mostrar mais quantos termos ?? [0 termina o programa]: '))
    cont = 0
    if adicional != 0:
        while cont < adicional:
            print(n)
            n += razao
            cont += 1
        nRepete = 1

