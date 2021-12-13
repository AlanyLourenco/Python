import random
a = str(input('Primeiro aluno: '))
b= str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))
Lista = [a, b, c, d]
Escolhido = random.choice(Lista)
print ('O aluno escolido foi {}'.format(Escolhido))
