from random import randint


def sorteia(números):
    """
    -> função que recebe a referencia de uma lista e preenche com 5 numeros aleatorios
    :param números: list()
    :return: sem retorno
    """
    if len(números) == 0:
        for c in range(0, 5):
            números.append(randint(0, 100))


def somapar(números):
    soma = 0
    if len(números) == 5:
        for num in números:
            if num % 2 == 0:
                soma += num
    print(f'a soma dos números pares é {soma}')


# main

números = list()
sorteia(números)
print(f'números sorteados para lista: {números}')
somapar(números)
