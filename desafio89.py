alunos = list()
boletim = list()

while True:
    nome = str(input('digite o nome do aluno: '))
    nota1 = float(input('digite a primeira nota: '))
    nota2 = float(input('digite a segunda nota: '))
    opcao = str(input('deseja continuar?[S/N]: '))
    boletim.append(nome)
    boletim.append(nota1)
    boletim.append(nota2)
    alunos.append(boletim[:])
    boletim.clear()
    if opcao.upper() != 'S':
        break

print('-=' * 23)
print('N°', ' ' * 5, 'Nome', ' ' * 5, 'Média')

for v, c in enumerate(alunos):
    media = (c[1] + c[2])/2
    nome = c[0]
    print(f'{v}', ' ' * 7, end='')
    print(f'{nome: <11}', end='')
    print(f'{media:.2f}')

while True:
    opcao = int(input('mostrar as notas de qual aluno?[999 interrompe]: '))
    if opcao == 999:
        break
    elif opcao > len(alunos) - 1 or opcao < 0:
        print('número inválido!!!')
    else:
        print(f'as notas de {alunos[opcao][0]} são {alunos[opcao][1]} e {alunos[opcao][2]}')