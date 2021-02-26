numeros = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete')
while True:
    escolha = int(input('digite um valor entre 1-7 para ser mostrado em extenso: '))
    if 7 >= escolha >= 1:
        print(numeros[escolha - 1])
    else:
        print('valor inválido')
