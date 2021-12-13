n=0
while True:
    n=int(input('Digite um numero: '))
    if n<0:
        break
    for c in range(1,11):
        print('{}  X  {} = {}'.format(c,n,(c*n))
    )
print('FIM')