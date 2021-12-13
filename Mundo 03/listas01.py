num=[1,2,3,0]
print(f'{num}')
for c,v in enumerate(num):
    print(f'Na posição {c+1} encontrei o valor {v}')
num[2]=5
print(f'{num}')
num.append(5)
print(f'{num}')
num.sort()
print(f'{num}')
num.sort(reverse=True)
print(f'{num}')
print(len(num))
num.insert(2,100)
print(f'{num}')
num.pop()
print(f'{num}')
num.pop(2)
print(f'{num}')
if 5 in num:
    num.remove(5)
else:
    print(f'Não foi encontrado o número 5')
print(f'{num}')

valor=list()
for cont in range(0,5):
    valor.append(int(input('Digite um valor: ')))
for c,v in enumerate(valor):
    print(f'Naposição {c+1} encontrei o valor {v}')

