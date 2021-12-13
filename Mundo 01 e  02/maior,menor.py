n=0
r='S'
cont=m=maior=menor=cont2=0
while r=='S':
    n=int(input('Digite um número: '))
    cont=cont+n
    cont2+=1
    if cont2==1:
        maior=menor=n
    else:
        if n> maior:
            maior=n
        if n< menor:
            menor=n
    r=str(input('Quer continuar? ')).strip().upper()[0]
print('SOMA ', (cont))
print('QUANTIDADE DE NUMEROS ', (cont2))
m=cont/cont2
print('MÉDIA', (m))
print('MAIOR ',(maior))
print('MENOR ',(menor))
    