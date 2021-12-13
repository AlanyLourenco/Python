matriz=[[0,0,0],[0,0,0],[0,0,0]]
pares=0
terceira=0
maior=0
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c]=int(input(f'Digite um valor: [{l} {c}]'))
for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for l in range (0,3):
    for c in range (0,3):
       if matriz[l][c]%2==0:
           pares= pares+matriz[l][c]
       if c==2:
           terceira=terceira+matriz[l][c]
       if l==1 and matriz[l][c]>maior:
           maior=matriz[l][c]
print(f'soma dos pares {pares}')
print(f'soma da terceira coluna da matriz {terceira}')
print(f'maior falor da terceira linha {maior}')
