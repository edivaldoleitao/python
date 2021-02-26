def leiaint(msg):

    while True:
        try:
            n = int(input(msg))
            break
        except KeyboardInterrupt:
            print('usuário não digitou o valor!')
            n = 0
            break
        except Exception as erro:
            print(f'foi localizado um erro do tipo: {erro.__class__}')
    return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
            break
        except KeyboardInterrupt:
            print('usuário não digitou o valor!')
            n = 0
            break
        except Exception as erro:
            print(f'foi encontrado um erro do tipo :{erro.__class__}')

    return n


# MAIN

# inteiro = leiaint('digite um número inteiro: ')
# real = leiafloat('digite um número real: ')

# print(f'o valor inteiro digitado foi {inteiro}, e o real foi {real}')


