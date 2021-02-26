def fatorial(numero, show=False):
    """
    -> calcula o fatorial e mostra os passos , dependendo do valor do parâmetro show
    :param numero: valor a ser calculado
    :param show: mostra ou não os passos do cálculo
    :return: não retorna nada
    """
    fat = 1
    if not show:
        while numero > 1:
            fat *= numero
            numero -= 1
        print(f'o fatorial é :{fat}')
    else:
        while numero > 1:
            fat *= numero
            numero -= 1
            print(f'{fat}*{numero}!', end='..')
        print(fat)
# MAIN


fatorial(5, True)
