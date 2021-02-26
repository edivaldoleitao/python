expressao = str(input('digite a expressão: '))
# RETIRA OS ESPAÇOS DA EXPRESSÃO PARA COLOCAR NA LISTA
expressao = expressao.replace(' ', '')

lista = []

parentesesE = parentesesD = 0

for c in range(0, len(expressao)):
    lista.append(expressao[c])

for caracter in lista:
    if caracter == '(':
        parentesesE += 1
    elif caracter == ')':
        parentesesD += 1

if parentesesE == parentesesD:
    print('\033[32mexpressão válida!!!')
else:
    print('\033[31mexpressão inválida!!!')