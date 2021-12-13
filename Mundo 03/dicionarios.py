#dicionario
#{}
#dados={'nome':'Pedro','idade':25}
#dados['sexo']='M'
#del dados['idade']
#print(dados.values())
#print(dados.keys())
#print(dados.items())

#for k,v in dados.items():
    #print(f'O {k} é {v}')
pessoas={'nome': 'Gustavo', 'sexo':'M','idade':22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

for k in pessoas.keys():
    print(k)
print('')
for k in pessoas.values():
    print(k)
print('')
for k,v in pessoas.items():
    print(f'{k} = {v}')
print('')
pessoas['nome']='Leandro'

for k,v in pessoas.items():
    print(f'{k} = {v}')

estado={}
brasil=[]
for c in range(0,3):
    estado['UF']=str(input('Unidade Federativa: '))
    estado['Sigla']=str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    print(e)
print('')
for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}')
print('')
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()

