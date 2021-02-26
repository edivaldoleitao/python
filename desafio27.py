nome = input('nome completo:')
print('o primeiro nome : {}'.format(nome.split()[0]))
print('o ultimo nome: {}'.format(nome[nome.rfind(' '):]))

