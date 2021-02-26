valorcasa = float(input('insira o valor da casa:'))
salario = float(input('insira o valor do seu salário de pobre!!'))
qtdAnos = int(input('número de anos que voçê vai tentar pagar, se puder!!!'))
valorParcelas = valorcasa/(qtdAnos*12)
if valorParcelas > salario*0.3:
    print('empréstimo negado')
else:
    print('o valor das parcelas fica {} R$'.format(valorParcelas))
