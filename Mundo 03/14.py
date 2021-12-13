from datetime import datetime
dados={}
dados['Nome']=str(input('Nome: '))
nasc=int(input('Ano de nascimento: '))
dados['Idade']=datetime.now().year-nasc
dados['CTPS']=int(input('Carteira de trabalho (0 = não tenho): '))
if dados['CTPS']!=0:
    dados['Contratação']=int(input('Ano de contratação: '))
    dados['Salário']=float(input('Salario: R$'))
    dados['Aposentadoria']=((dados['Contratação']+35)- datetime.now().year)+dados['Idade']
print()
for k,v in dados.items():
    print(f'{k} tem o valor {v}')