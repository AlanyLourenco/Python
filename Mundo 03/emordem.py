lista=[]
for c in range(0,5):
    n=int(input(f'Digite um valor: '))
    if c==0 or n> lista[len(lista)-1]:
        lista.append(n)
        print('Adicionado no final da lista')
    else:
        posi=0
        while posi<len(lista):
            if n<= lista[posi]:
                lista.insert(posi,n)
                print(f'Adicionado na posição {posi+1}')
                break
            posi+=1
print(f'Os valores digitados em ordem foram: {lista}')