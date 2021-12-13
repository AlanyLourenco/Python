temp=[]
lista=[]
mai=men=0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(lista)==0:
        mai=men=temp[1]
    else:
        if temp[1]>mai:
            mai=temp[1]
        if temp[1]<men:
            men=temp[1]
    lista.append(temp[:])
    temp.clear()
    resp=str(input('Quer continuar s/n: ')).upper()
    if resp not in 'SIM':
        break
print(f'Você cadastrou {len(lista)} pessoas')
print(f'O maior peso foi {mai} kg e o menor {men} kg')
for p in lista:
    if p[1]== mai:
        print(f'{ p[0] }, ', end='')
print(f'foram os mais pesados')
for p in lista:
    if p[1]== men:
        print(f'{ p[0] }, ', end='')
print(f'foram os menos pesados')