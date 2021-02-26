lista = []
maior = menor = 0
for c in range(0, 5):
    elemento = int(input('digite um valor: '))
    if c == 0:
        lista.append(elemento)
        menor = maior = elemento
        print('o valor foi adicionado na posição 0 da lista')
    elif menor >= elemento:
        menor = elemento
        lista.insert(0, menor)
        print('foi adicionado na posição 0 da lista')
    elif maior <= elemento:
        maior = elemento
        lista.append(maior)
        print(f'foi adicionado na posição {len(lista) - 1} da lista')
    else:
        for v, l in enumerate(lista):
            if l >= elemento:
                lista.insert(v, elemento)
                print(f'foi adicionado na posição {v} da lista')
                break
print(len(lista))
print(lista)
