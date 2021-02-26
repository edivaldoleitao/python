nomeMenor = ''
precoMenor = 0
countCaros = 0
total = 0
while True:
    print(f'{"":->40}\n {"mecador maneiro":^40} \n{"":->40}')
    nome = str(input('nome do produto: '))
    preco = float(input('digite o preço do produto: '))
    if preco >= 1000:
        countCaros += 1
    if total == 0:
        precoMenor = preco
        nomeMenor = nome
    elif precoMenor > preco:
        precoMenor = preco
        nomeMenor = nomeMenor
    total += preco
    opcao = str(input('deseja continuar?[S/N]: '))
    if opcao.upper() != 'S':
        break
print(f'{"":->40}\nmenor preço do produto: {precoMenor}\nnome do produto de menor preço: {nomeMenor}\nquantidade de produtos acima de 1000 R$: {countCaros}\no total: {total}\n{"":->40}')
