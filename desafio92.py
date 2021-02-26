from datetime import datetime

empregado = dict()
empregado['nome'] = str(input('digite seu nome: '))
empregado['anoNascimento'] = int(input('digite o ano de nascimento: '))
empregado['ctps'] = int(input('digite o número da sua carteira de trabalho[0 caso não tenha]: '))
empregado['idade'] = datetime.now().year - empregado['anoNascimento']
if empregado['ctps'] != 0:
    empregado['anoContratacao'] = int(input('digite seu ano de contratação: '))
    empregado['aposentadoria'] = empregado['idade'] + 35
empregado['salario'] = float(input('digite seu salário: '))

print('\033[31m-=\033[m' * 83)

print(empregado)

for k, v in empregado.items():
    print(f'{k} tem valor {v}')
