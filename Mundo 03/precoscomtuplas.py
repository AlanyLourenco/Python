listagem=('Lapis',1.75,'Cadernor',15.90,'Borracha',2,'Compasso',9.99)
print('_'*38)
print('')
print(f'{"LISTAGEM DE PREÇOS":^38}')
print('_'*38)
for posi in range(0,len(listagem)):
   if posi%2==0:
        print(f'{listagem[posi]:.<30}', end='')
   else:
       print(f' R${listagem[posi]:>5.2f}')
