lista=[]
while True:
   lista.append(int(input('Digite um número: ')))
   r=str(input('Deseja comtinuar? digite sim ou não: ')).upper()
   if r!='SIM':
        break
print(f'{len(lista)}')
lista.sort(reverse=True)
print(f'{lista}')
if 5 in lista:
    print(f'O numero 5 foi digitado')
else:
    print(f'O numero 5 não foi encontador')