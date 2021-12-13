from time import sleep
def maior(*num):
    cont=maior=0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='',flush=True)
        sleep(0.3)
        if cont==0:
            maior=valor
        else:
            if valor>maior:
                maior=valor
        cont+=1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2,9,4,7,1)
maior(1,6,8,2,8745,485,451,85)
maior(4,85,56,5,12,55120,5543)