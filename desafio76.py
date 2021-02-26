produtosPrecos = ('peixe', 'carne', 'leite', (1.40, 1.74, 1.90))
# centralização com preenchimento de "-", usando formatação de strings
print(f'{"tabela de preços":-^40}')
# usando fstrings para formatar as mensagens
for c in range(0, len(produtosPrecos) - 1):
    print(f'{produtosPrecos[c]} {"." * 20}R$ {produtosPrecos[len(produtosPrecos) - 1][c]}')
print('-' * 40)
