import random
a = str(input('Primeiro aluno: '))
b= str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))
Lista = [a, b, c, d]
random.shuffle(Lista)
print('A ordem embaraçhada será: ')
print(Lista)