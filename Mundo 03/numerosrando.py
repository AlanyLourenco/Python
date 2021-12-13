from random import randint
numeros=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)) #parenteses para tupla, repete o numero de randints para a quantidade de numeros que se deseja 
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)}')
