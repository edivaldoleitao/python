wage = float(input(' digite o seu salário:'))
if wage > 1250:
    raised = wage*0.1
else:
    raised = wage*0.15
print('o seu aumento foi de {} R$'.format(raised))

