numeros= list()
while True:
    n=int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print(f'Valor ja existe não vou adicionar')
    r=str(input('Deseja comtinuar? digite sim ou não: ')).upper()
    if r!='SIM':
        break
print(f'{numeros}')
numeros.sort()
print(f'{numeros}')