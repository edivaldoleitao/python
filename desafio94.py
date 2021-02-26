pessoa = dict()
listaPessoas = list()

while True:
    pessoa['nome'] = str(input('digite o nome: '))
    pessoa['idade'] = int(input('digite a idade: '))
    pessoa['sexo'] = str(input('digite o sexo[M/F]: '))
    opcao = str(input('deseja continuar?[S/N]: '))
    listaPessoas.append(pessoa.copy())
    if opcao.upper() != 'S':
        break

idadeMedia = 0

for p in listaPessoas:
    idadeMedia += p['idade']

idadeMedia = idadeMedia/len(listaPessoas)

print('=-' * 83)
print(f'foram cadastradas {len(listaPessoas)} pessoas , a idade média é {idadeMedia:.2f} anos ')
print('as mulheres são:')

for p in listaPessoas:
    if p['sexo'].upper() == 'F':
        print(f'\t{p["nome"]}')

print('-=' * 83)
print('pessoas com idade acima da média')

for p in listaPessoas:
    if p['idade'] > idadeMedia:
        print(f'\t{p["nome"]}')
