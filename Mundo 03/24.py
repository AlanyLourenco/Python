def fat(fatot,show):
    f=1
    for c in range(fatot,0,-1):
        f*=c
    print(f)
    if show==True:
        for c in range(fatot,0,-1):
            if c!=1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = {f}')
    


fato=int(input('Digite um número para obter o fatorial: '))
tf=str(input('Você deseja ver o processo? ')).upper()
if tf in 'S':
    show=True
else:
    show=False
fat(fato,show)
