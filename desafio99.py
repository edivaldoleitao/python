def mostramaior(* num):
    lista = sorted(num, reverse=True)
    print('os valores foram: ', end='')
    for c in lista:
        print(c, end=' ')
    print(f'\no maior é {lista[0]}')



# PROGRAMA MAIN
mostramaior(1, 2, 3, 4, 9)

