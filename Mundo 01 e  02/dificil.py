n=int(input('Digite o primeiro número '))
m=int(input('Digitr o segundo número '))
j=0
while j!=5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR''')
    j=int(input('Qual a sua opção? '))
    if j==1:
        print(m+n)
    elif j==2:
        print(m*n)
    elif j==3:
        if m>n:
            maior=m
        elif m==n:
            print('iguais')
        else:
            maior=n
    elif j==4:
        n=int(input('Digite o primeiro número '))
        m=int(input('Digitr o segundo número '))
    elif j==5:
        print('fim')
print('fim')
