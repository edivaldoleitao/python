aluno = dict()
aluno['nome'] = str(input('digite o nome do aluno: '))
aluno['media'] = float(input('digite a média do aluno: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
else:
    aluno['situacao'] = 'reprovado'

print(f'o nome é {aluno["nome"]} , a média é {aluno["media"]} e a situação é {aluno["situacao"]}')