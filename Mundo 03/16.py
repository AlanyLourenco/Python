galera=[]
pessoas={}
soma=media=0
while True:
    pessoas.clear()
    pessoas['Nome']= str(input('Nome: '))
    while True:
        pessoas['Sexo']= str(input('Sexo: [M/F] ')).upper()[0]
        if pessoas['Sexo'] in 'MF':
            break
        print('Erro! \nPor favor, digite apenas M ou F')
    pessoas['Idade']= int(input('Idade: '))
    soma+=pessoas['Idade']
    galera.append(pessoas.copy())
    while True:
        resposta=str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resposta in 'SN':
            break
        print('Erro! \nPor favor, digite apenas S ou N')
    if resposta=='N':
        break
print('+='*23)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media=soma/len(galera)
print('+='*23)
print(f'A média de idade é de {media:5.2f} anos')
print('+='*23)
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}, ', end='')
print()   
print('+='*23)
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['Idade']>= media:
        for k,v in p.items():
            print(f'{k}={v}: ', end='')
        print()
print('+='*23)
print('<<Encerado>>')
print('+='*23)
