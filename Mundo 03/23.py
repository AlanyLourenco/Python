from datetime import datetime

def voto(nasc):
    ida=datetime.now().year-nasc
    if (ida>=16 and ida<18) or ida>65:
        print(f'Com {ida} anos: Voto opcional') 
    elif ida>=18 and ida<=65:
        print(f'Com {ida} anos: Voto obrigatório')
    else:
        print(f'Com {ida} anos: Não se pode votar')


nasc=int(input('Digite o seu ano de nascimento: '))
voto(nasc)

