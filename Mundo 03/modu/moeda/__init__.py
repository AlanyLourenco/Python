def metade(n=0,formato=False):
    m=n/2

    return m if formato is False else moeda(m)


def dobro(n=0,formato=False):
    m=n*2
    return m if formato is False else moeda(m)


def mais(n=0,d=0,formato=False):
    m=((d/100)*n)+n
    return m if formato is False else moeda(m)


def desc(n=0,d=0,formato=False):
    m=n-((d/100)*n)
    return m if formato is False else moeda(m)


def moeda(preço=0,moed='R$',formato=False):
    return f'{moed}{preço:>.2f}'.replace('.',',')


def resumo(n=0,up=10,do=10):
    print('='*30)
    print(f'O dobro de {moeda(n)} é: \t{dobro(n,True)} ')
    print(f'A metade do {moeda(n)} é: \t{metade(n,True)} ')
    print(f'Aumento de {up}% é: \t{mais(n,up,True)} ')
    print(f'Desconto de {do}% é: \t{desc(n,do,True)} ')
    print('='*30)