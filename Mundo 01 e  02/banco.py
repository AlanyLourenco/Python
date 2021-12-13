print('='*30)
print('{:^30}'.format('BANCO'))
print('='*30)
valor=int(input('Que valor você quer sacar? R$'))
total=valor
ced5=50
totced5=0
while True:
    if total>=ced5:
        total-=ced5
        totced5+=1
    else:
        if totced5>0:
            print(f'Total de {totced5} cédulas de R$ {ced5}')
        if ced5==50:
            ced5=20
        elif ced5==20:
            ced5=10
        elif ced5==10:
            ced5=1
        totced5=0
        if total==0:
            break
        