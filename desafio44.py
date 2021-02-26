preco = float(input('digite o preço do produto:'))
opcao = int(input('escolha uma opcao de pagamento: \n 1-à vista \n 2-à vista no cartão \n 3-parcelado no cartão em até 2x\n 4-parcelado no cartão a partir de 3x'))
if opcao == 1:
    print('pagamento será de {:.2f}'.format(preco*0.9))
elif opcao == 2:
    print('o pagamento será de {:.2f}'.format(preco*0.95))
elif opcao == 3:
    print('o pagamento será de {:.2f}'.format(preco))
elif opcao == 4:
    print('o pagamento será de {:.2f}'.format(preco*1.20))

