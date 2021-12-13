from time import sleep
def cont(a,b,c):
    if c<0:
        c*=-1
    if c==0:
        c=1
    print(f'Contagem de {a} até {b} de {c} em {c}')
    sleep(2)
    if a<b:
        conta=a
        while conta<=b:
            print(f'{conta} ', end='',flush=True)
            sleep(0.5)
            conta+=c
        print('fim!')
    else:
        conta=a
        while conta>=b:
            print(f'{conta} ', end='',flush=True)
            sleep(0.5)
            conta-=c
        print('fim!')



cont(1,10,1)
print()
cont(10,0,2)
print()
print('Sua vez de personalizar')
i=int(input('Inicio: '))
f=int(input('Fim:    '))
p=int(input('Salto:  '))
print()
cont(i,f,p)
