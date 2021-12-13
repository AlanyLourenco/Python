a=int(input('Digite um número: '))
b=int(input('Digite um número: '))
if a>b:
    print('O primeiro número {} é maior que {}'.format(a,b))
elif a<b:
    print('o segundo número {} é maior que {}'.format(b,a))
elif a==b:
    print('{} igual a {}'.format(a,b))
    