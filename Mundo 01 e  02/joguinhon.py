import random, time
comp= random.randint(0, 10)
print('pensei em um numero entre 0 e 10, tente acertar qual numero é')
acert=False
palpite=0
while not acert:
    j=int(input('Qual é o seu palpite: '))
    palpite=palpite+1
    if j==comp:
        acert=True
    else:
        if j<comp:
            print('Mais... Tente mais uma vez')
        if j>comp:
            print('menor... Tente mais uma vez')
print('Acertou com {} tentativas'.format(palpite))
