palavras = ('carro', 'time', 'computador', 'livro', 'casa', 'ventilador', 'gaveta', 'porta', 'cortina', 'cama', 'mouse',
            'teclado', 'prancha', 'gibi', 'boneco',)
vogais = ('a', 'e', 'i', 'o', 'u')

for palavra in palavras:
    print(f'{palavra} tem essas vogais: ', end='')
    for vogal in vogais:
        if vogal in palavra:
            print(f'{vogal},', end=' ')
    print('')
