num=[]
men=0
max=0
for c in range(0,5):
    num.append(int(input('Digite um número: ')))
    if c==0:
        men=maxi=num[c]
    else :
        if num[c]>maxi:
            maxi=num[c]
        if num[c]<men:
            men=num[c]
print(f'O maior valor é {maxi} e o menor é {men}')
print(f'O maior valor esta na posição: ')
for i,v in enumerate(num):
    if v==maxi:
        print(i+1, )
print(f'O menor valor esta na posição: ')        
for i,v in enumerate(num):
    if v==men:
        print(i+1, )


