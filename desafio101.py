def voto(ano_nascimento):
    # é possível importar só no escopo da função
    from datetime import datetime
    data_atual = datetime.today().year
    diferenca_data = data_atual - ano_nascimento
    return diferenca_data


# MAIN
voto_opc = voto(2020)
if voto_opc < 16:
    print(f'com {voto_opc} anos => VOTO NEGADO')
elif voto_opc >= 60:
    print(f'com {voto_opc} anos => VOTO OPCIONAL')
else:
    print(f'com {voto_opc} anos => VOTO OBRITGATÓRIO')
