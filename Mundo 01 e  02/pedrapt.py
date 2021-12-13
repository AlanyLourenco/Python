import random, time 
i=('Pedra','Papel','Tesoura')
c= random.randint(0,2)
print('''Suas opções:
[0] Pedra 
[1] Papel
[2] Tesoura''')
j=int(input('Qual a sua jogada? '))
print('Jogando...')
time.sleep(1)
print('.')
time.sleep(1)
print('..')
time.sleep(1)
print('...')
time.sleep(1)
print('--'*16)
print('vocẽ jogou {}'.format(i[j]))
print('O computador escolheu {}'.format(i[c]))
print('--'*16)
if c==0:
    if j==0:
        print('\033[1;31;42mEmpate\033[m')
    elif j==1:
        print('\033[1;32mVocê venceu\033m[')
    elif j==2:
        print('\033[1;31mVocê perdeu\033[m')
    else:
        print('Jogada invalida')
elif c==1:
    if j==0:
        print('\033[1;31mVocê perdeu\033[m')
    elif j==1:
        print('\033[1;31;42mEmpate\033[m')
    elif j==2:
        print('\033[1;32;31mVocê venceu\033[m')
    else:
        print('Jogada invalida')
elif c==2:
    if j==0:
        print('\033[1;32mVocê venceu\033[m')
    elif j==1:
        print('\033[1;31mVocê perdeu\033[m')
    elif j==2:
        print('\033[1;31;42mEmpate\033[m')
    else:
        print('Jogada invalida')
        