n=int(input('Qual o primeiro termo de uma PA? '))
r=int(input('Qual a razão da sua PA? '))
termo=n
cont=1
total=0
mais=5
while mais!=0:
    total= total+ mais
    while cont<=total:
        print(termo)
        termo+=r
        cont=cont+1
    print('pausa')  
    mais=int(input('Quantos termos você quer mostra? '))
print('{} termos mostrados'.format(total))
