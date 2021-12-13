lista=[]
par=[]
impar=[]
while True:
   lista.append(int(input('Digite um número: ')))
   r=str(input('Deseja comtinuar? digite s ou n: ')).upper()
   if r!='S':
        break
n=len(lista)
for c in range(0,n):
    if (lista[c])%2==0:
        par.append(lista[c])
    else:
        impar.append(lista[c])
print(lista)
print(par)
print(impar)
