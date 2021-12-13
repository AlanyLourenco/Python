jogador={}
partidas=[]
time=[]
while True:
    jogador.clear()
    jogador['Nome']=str(input('Nome do jogador: '))
    tot=int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['Gols']=partidas[:]
    jogador['Total']=sum(partidas)
    time.append(jogador.copy())
    while True:
        resp=str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.' )
    if resp=='N':
        break
print()
print('COD ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k,v in enumerate(time):
    print(f'{k+1:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print()
while True:
    busca= int(input('Mostrar dados de qual jogador? (999) para parar: '))
    if busca==999:
       break
    if busca>len(time):
        print(f'Erro! Não existe jogador com o codgo {busca}')
    else:
        print(f'Levantamennto do jogator {time[busca-1]["Nome"]}: ')
        for i,g in enumerate (time[busca-1]['Gols']):
            print (f'No jogo {i+1} fez g gols.')
        print()
print('Volte sempre')



