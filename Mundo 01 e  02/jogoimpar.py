import random
comp= random.randint(0,10)
n=0
s=0
while True:
    n=int(input('Escolha um número: '))
    jogador=str(input('PAR OU IMPAR ')).strip().upper()
    print(f'O computador escolheu {comp}')
    if jogador== 'PAR':
         c='IMPAR'
    else:
        c='PAR'
    s=n+comp
    if s%2==0 and jogador=='PAR' or s%2==1 and jogador=='IMPAR':
        print(f'A soma foi {s} {jogador}\n Você ganhou\n Vamos jogar novamente...')
    else:
        print(f'A soma foi {s} {c}\n Você perdeu')
        break
print('Fim do jogo')